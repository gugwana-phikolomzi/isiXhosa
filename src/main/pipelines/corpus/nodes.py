import re
import pandas as pd
from kedro.pipeline import Pipeline, node

def _to_text_series(df: pd.DataFrame) -> pd.Series:
    """
    Normalize any 1+ column DataFrame to a clean 'text' Series.
    - Prefer 'text' column; else 'sentence'; else first column.
    - Strip, replace newlines with spaces, collapse runs of spaces.
    - Drop empty rows.
    """
    if "text" in df.columns:
        col = "text"
    elif "sentence" in df.columns:
        col = "sentence"
    else:
        col = df.columns[0]

    s = df[col].astype(str).str.strip()
    s = s.str.replace("\n", " ", regex=False)
    s = s.str.replace(r"\s{2,}", " ", regex=True)
    s = s[s.ne("")]
    return s

def concat_corpora(
    isiXhosa_sentences: pd.DataFrame,
    bible_text_corpus: pd.DataFrame,
    data_source_3: pd.DataFrame,   # <-- NEW
) -> pd.DataFrame:
    """
    Concatenate DoBE, Bible, and Data_source_3 corpora into a single-column DataFrame 'text'.
    """
    s1 = _to_text_series(isiXhosa_sentences)
    s2 = _to_text_series(bible_text_corpus)
    s3 = _to_text_series(data_source_3)   # <-- NEW
    combined = pd.concat([s1, s2, s3], ignore_index=True)
    return combined.to_frame(name="text")
