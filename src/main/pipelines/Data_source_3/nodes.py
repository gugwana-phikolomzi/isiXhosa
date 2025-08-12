import re
import pandas as pd

def _to_text_only(df: pd.DataFrame) -> pd.Series:
    """Return a cleaned 'text' Series from a 2-col 'web link|text' CSV."""
    s = df["text"] if "text" in df.columns else df.iloc[:, -1]
    s = s.astype(str)
    # remove surrounding double quotes only
    s = s.str.replace(r'^\s*"(.*)"\s*$', r"\1", regex=True)
    # normalize whitespace/newlines
    s = s.str.replace("\n", " ", regex=False)
    s = s.str.replace(r"\s{2,}", " ", regex=True)
    return s

_sentence_splitter = re.compile(r"(?<=[.!?])\s+")

def _split_into_sentences(text: str) -> list[str]:
    """Basic sentence split on ., !, ? followed by whitespace."""
    if not text:
        return []
    parts = _sentence_splitter.split(text)
    # trim, drop empty, strip surrounding quotes
    parts = [p.strip().strip('"').strip("'") for p in parts]
    return [p for p in parts if p]

def combine_texts(entsimini: pd.DataFrame,
                  ezemidlalo: pd.DataFrame,
                  ezoyolo: pd.DataFrame) -> pd.DataFrame:
    # 1) collapse each input to a clean 'text' Series
    parts = [
        _to_text_only(entsimini),
        _to_text_only(ezemidlalo),
        _to_text_only(ezoyolo),
    ]
    all_text = pd.concat(parts, ignore_index=True)
    all_text = all_text[all_text.astype(str).str.strip().ne("")]

    # 2) split into sentences
    sentences = []
    seen = set()
    for t in all_text:
        for s in _split_into_sentences(t):
            key = s.lower()
            if key not in seen:
                seen.add(key)
                sentences.append(s)

    # 3) return one sentence per row
    return pd.DataFrame({"sentence": sentences})
