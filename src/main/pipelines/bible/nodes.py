import re
import pandas as pd

# --- helpers ---
_sentence_splitter = re.compile(r"(?<=[.!?])\s+")

def _clean_text_series(s: pd.Series) -> pd.Series:
    s = s.astype(str).str.strip()
    # remove only surrounding double quotes if present
    s = s.str.replace(r'^\s*"(.*)"\s*$', r"\1", regex=True)
    # normalize whitespace/newlines
    s = s.str.replace("\n", " ", regex=False)
    s = s.str.replace(r"\s{2,}", " ", regex=True)
    # drop blanks
    s = s[s.str.strip().ne("")]
    return s

def _split_into_sentences(text: str) -> list[str]:
    if not text:
        return []
    parts = _sentence_splitter.split(text)
    parts = [p.strip().strip('"').strip("'") for p in parts]
    return [p for p in parts if p]

# --- node ---
def select_and_concat_textframes(xho75: pd.DataFrame,
                                 xho96: pd.DataFrame,
                                 xho1902a: pd.DataFrame) -> pd.DataFrame:
    """
    Input: three dataframes each with a 'text' column.
    Output: one sentence per row in column 'sentence', deduped case-insensitively.
    (Dedup uses lowercase keys only for comparison—original casing is preserved.)
    """
    def only_text(df: pd.DataFrame) -> pd.Series:
        if "text" not in df.columns:
            raise KeyError("Expected a 'text' column in input CSV.")
        return _clean_text_series(df["text"])

    # 1) clean and concatenate text
    all_text = pd.concat(
        [only_text(xho75), only_text(xho96), only_text(xho1902a)],
        ignore_index=True
    )

    # 2) split into sentences and dedupe (case-insensitive)
    sentences, seen = [], set()
    for t in all_text:
        for s in _split_into_sentences(t):
            key = s.lower()
            if key not in seen:
                seen.add(key)
                sentences.append(s)

    # 3) return one sentence per row
    return pd.DataFrame({"sentence": sentences})
