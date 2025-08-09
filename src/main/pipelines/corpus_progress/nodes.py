import glob
import os
import re
import hashlib
from typing import Dict, Tuple
import pandas as pd
import logging
logger = logging.getLogger(__name__)


# Try tiktoken; fall back to a chars-per-token heuristic
try:
    import tiktoken
    _ENC = tiktoken.get_encoding("gpt2")
    def _count_tokens(text: str) -> int:
        return len(_ENC.encode(text))
except Exception:
    _ENC = None
    def _count_tokens(text: str) -> int:
        # Conservative isiXhosa-ish average (fewer tokens than English per char)
        return max(1, int(len(text) / 3.8))

# Milestones
MILESTONES = [
    ("Toy demo",               10_000_000),   # ~10M tokens
    ("Usable (baseline)",     100_000_000),   # ~100M tokens
    ("Genuinely useful",      500_000_000),   # ~500M tokens
    ("Strong small model",  1_000_000_000),   # ~1B tokens
]

CLEAN_RE = re.compile(r"[ \t]+")
NEWLINE_RE = re.compile(r"\n+")

def _normalize(text: str) -> str:
    text = text.replace("\r", "\n")
    text = CLEAN_RE.sub(" ", text)
    text = NEWLINE_RE.sub("\n", text).strip()
    return text

def _doc_hash(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()
def analyze_corpus_partition(
    corpus: Dict[str, str],
    dedup: bool = True,
    min_doc_chars: int = 200,
    report_title: str = "isiXhosa Corpus Progress"
):
    records = []
    seen = set()
    total_tokens = total_chars = total_words = kept_docs = 0

    for path, text in corpus.items():
        if not isinstance(text, str):
            try:
                text = text.decode("utf-8")
            except Exception:
                continue

        raw_bytes = len(text.encode("utf-8"))
        norm = _normalize(text)
        if len(norm) < min_doc_chars:
            continue

        h = _doc_hash(norm)
        if dedup and h in seen:
            records.append({
                "path": path, "kept": False, "reason": "duplicate",
                "raw_bytes": raw_bytes, "chars": len(norm),
                "words": len(norm.split()), "tokens_est": 0,
            })
            continue

        seen.add(h)
        tokens = _count_tokens(norm)
        words = len(norm.split()); chars = len(norm)
        total_tokens += tokens; total_words += words; total_chars += chars; kept_docs += 1
        records.append({
            "path": path, "kept": True, "reason": "ok",
            "raw_bytes": raw_bytes, "chars": chars,
            "words": words, "tokens_est": tokens,
        })

    # Build per-file df robustly
    expected_cols = ["path","kept","reason","raw_bytes","chars","words","tokens_est"]
    df = pd.DataFrame.from_records(records)
    if df.empty:
        logger.warning("[corpus_progress] No documents kept (empty corpus, all too short, or all duplicates).")
        df = pd.DataFrame(columns=expected_cols)
    if "path" in df.columns:
        df = df.sort_values("path")

    # Milestones
    def pct_of(target): 
        return min(100.0, 100.0 * total_tokens / target) if target else 0.0

    milestones = []
    for name, target in MILESTONES:
        milestones.append({
            "milestone": name,
            "target_tokens": target,
            "progress_tokens": total_tokens,
            "progress_%": round(pct_of(target), 2),
            "remaining_tokens": max(0, target - total_tokens),
        })
    ms_df = pd.DataFrame(milestones)

    # Markdown
    def human_bytes(n):
        units = ["B","KB","MB","GB","TB"]; i = 0
        n = float(n)
        while n >= 1024 and i < len(units)-1:
            n /= 1024.0; i += 1
        return f"{n:.2f} {units[i]}"

    lines = []
    lines.append(f"# {report_title}\n")
    lines.append(f"**Tokenizer:** {'tiktoken/gpt2' if _ENC else 'heuristic (chars/3.8)'}\n")
    lines.append("## Corpus Summary")
    lines.append(f"- **Documents (kept):** {kept_docs}")
    lines.append(f"- **Total characters:** {total_chars:,}")
    lines.append(f"- **Estimated tokens:** {total_tokens:,}")
    lines.append(f"- **Approx raw size:** {human_bytes(total_chars)}\n")
    lines.append("## Milestones")
    for _, row in ms_df.iterrows():
        lines.append(
            f"- **{row['milestone']}** — target **{int(row['target_tokens']):,}** · "
            f"progress **{int(row['progress_tokens']):,}** (**{row['progress_%']:.2f}%**) · "
            f"remaining **{int(row['remaining_tokens']):,}**"
        )
    lines.append("\n## Notes")
    lines.append("- Counts will shift once we train an isiXhosa tokenizer (usually fewer tokens than GPT‑2).")
    lines.append("- Current dedup is exact hash; consider near-dup later (MinHash/LSH).")
    report_md = "\n".join(lines)

    return df, ms_df, report_md



import glob
import os
import logging
from typing import Dict
import pandas as pd

logger = logging.getLogger(__name__)

def load_corpus_from_fs(corpus_root: str, file_glob: str, text_column: str) -> Dict[str, str]:
    import glob, os, logging
    import pandas as pd
    logger = logging.getLogger(__name__)

    root_abs = os.path.abspath(corpus_root)
    pattern = os.path.join(corpus_root, file_glob)
    pattern_abs = os.path.abspath(pattern)
    paths = glob.glob(pattern, recursive=True)

    logger.info(f"[corpus_progress] corpus_root abs: {root_abs}")
    logger.info(f"[corpus_progress] glob pattern abs: {pattern_abs}")
    logger.info(f"[corpus_progress] matched {len(paths)} file(s): {paths[:10]}")

    corpus: Dict[str, str] = {}
    samples = []

    for p in paths:
        ext = os.path.splitext(p)[1].lower()

        if ext == ".txt":
            try:
                with open(p, "r", encoding="utf-8") as f:
                    txt = f.read()
                corpus[p] = txt
                if len(samples) < 3 and txt.strip():
                    samples.append(txt.strip()[:120])
            except Exception as e:
                logger.warning(f"[corpus_progress] Skipping TXT {p}: {e}")

        elif ext == ".csv":
            try:
                # try with header first
                df = pd.read_csv(p, dtype=str, on_bad_lines="skip", engine="python")
                use_col = None
                if text_column in df.columns:
                    use_col = text_column
                else:
                    # retry headerless
                    df2 = pd.read_csv(p, header=None, dtype=str, on_bad_lines="skip", engine="python")
                    if text_column in df2.columns.astype(str).tolist():
                        df = df2
                        use_col = text_column
                    elif df2.shape[1] == 1:
                        df = df2
                        use_col = df.columns[0]

                if use_col is None:
                    logger.warning(f"[corpus_progress] CSV {p}: text column '{text_column}' not found; cols(header): {list(df.columns)}")
                    continue

                loaded_rows = 0
                for i, val in df[use_col].items():
                    s = (val or "").strip()
                    if s:
                        key = f"{p}#row{i}"
                        corpus[key] = s
                        loaded_rows += 1
                        if len(samples) < 3:
                            samples.append(s[:120])

                logger.info(f"[corpus_progress] CSV {p}: loaded {loaded_rows} non-empty rows from column '{use_col}'")

            except Exception as e:
                logger.warning(f"[corpus_progress] Skipping CSV {p}: {e}")

        else:
            logger.info(f"[corpus_progress] Ignoring non-text file: {p}")

    logger.info(f"[corpus_progress] TOTAL documents loaded: {len(corpus)}")
    if samples:
        logger.info(f"[corpus_progress] First samples: {samples}")

    return corpus




def corpus_progress_node(
    corpus_root: str,
    file_glob: str,
    dedup: bool,
    min_doc_chars: int,
    report_title: str,
    text_column: str  # NEW
):
    corpus = load_corpus_from_fs(corpus_root, file_glob, text_column)
    return analyze_corpus_partition(
        corpus=corpus,
        dedup=dedup,
        min_doc_chars=min_doc_chars,
        report_title=report_title
    )
