import pandas as pd
import re

def clean_exam_data(
    # --- 2008 (first sitting) ---
    fal_p1: str,
    fal_p1_memo: str,
    fal_p3: str,
    hl_p1: str,
    hl_p1_memo: str,
    hl_p3: str,
    sal_p1_eastern_cape: str,
    sal_p1_eastern_cape_memo: str,
    sal_p1_gauteng: str,
    sal_p1_gauteng_memo: str,
    sal_p1_western_cape: str,
    sal_p1_western_cape_memo: str,
    sal_p2_memo: str,

    # --- 2008_1 (November 2008) ---
    fal_p1_2008_1: str,
    fal_p1_memo_2008_1: str,
    fal_p3_2008_1: str,
    hl_p1_2008_1: str,
    hl_p1_memo_2008_1: str,
    hl_p3_2008_1: str,
    sal_p1_eastern_cape_2008_1: str,
    sal_p1_eastern_cape_memo_2008_1: str,
    sal_p1_gauteng_2008_1: str,
    sal_p1_gauteng_memo_2008_1: str,
    sal_p1_western_cape_2008_1: str,
    sal_p1_western_cape_memo_2008_1: str,
    sal_p2_memo_2008_1: str,

    # --- 2009 ---
    fal_p1_2009_memo: str,
    fal_p1_2009_paper: str,
    fal_p3_2009_paper: str,
    fal_p3_2009_rubric: str,
    hl_p1_2009_paper: str,
    hl_p2_2009_memo: str,
    hl_p2_2009_paper: str,
    hl_p3_2009_paper: str,
    hl_p3_2009_rubric: str,
    sal_p2_2009_paper: str,
    sal_p2_2009_rubric: str,
    sal_p1_2009_eastern_cape: str,
    sal_p1_2009_western_cape: str,

    # --- 2011 (first sitting) ---
    fal_p1_2011_memo: str,
    fal_p1_2011_paper: str,
    fal_p2_2011_memo: str,
    fal_p2_2011_paper: str,
    fal_p3_2011_memo: str,
    fal_p3_2011_paper: str,
    hl_p1_2011_memo: str,
    hl_p1_2011_paper: str,
    hl_p2_2011_memo: str,
    hl_p2_2011_paper: str,
    hl_p3_2011_memo: str,
    hl_p3_2011_paper: str,
    sal_p1_2011_eastern_cape: str,
    sal_p2_2011_memo: str,
    sal_p2_2011_paper: str,

    # --- 2011_1 (November 2011) ---
    fal_p1_2011_1: str,
    fal_p2_2011_1: str,
    fal_p3_2011_1: str,
    hl_p1_2011_1: str,
    hl_p2_2011_1: str,
    hl_p3_2011_1: str,
    sal_p1_2011_1_eastern_cape: str,
    sal_p1_2011_1_western_cape: str,
    sal_p2_2011_1: str,
) -> pd.DataFrame:
    records = [
        # --- 2008 ---
        ("2008 FAL P1", fal_p1),
        ("2008 FAL P1 Memo", fal_p1_memo),
        ("2008 FAL P3", fal_p3),
        ("2008 HL P1", hl_p1),
        ("2008 HL P1 Memo", hl_p1_memo),
        ("2008 HL P3", hl_p3),
        ("2008 SAL P1 Eastern Cape", sal_p1_eastern_cape),
        ("2008 SAL P1 Eastern Cape Memo", sal_p1_eastern_cape_memo),
        ("2008 SAL P1 Gauteng", sal_p1_gauteng),
        ("2008 SAL P1 Gauteng Memo", sal_p1_gauteng_memo),
        ("2008 SAL P1 Western Cape", sal_p1_western_cape),
        ("2008 SAL P1 Western Cape Memo", sal_p1_western_cape_memo),
        ("2008 SAL P2 Memo", sal_p2_memo),

        # --- 2008_1 (November) ---
        ("2008_1 FAL P1", fal_p1_2008_1),
        ("2008_1 FAL P1 Memo", fal_p1_memo_2008_1),
        ("2008_1 FAL P3", fal_p3_2008_1),
        ("2008_1 HL P1", hl_p1_2008_1),
        ("2008_1 HL P1 Memo", hl_p1_memo_2008_1),
        ("2008_1 HL P3", hl_p3_2008_1),
        ("2008_1 SAL P1 Eastern Cape", sal_p1_eastern_cape_2008_1),
        ("2008_1 SAL P1 Eastern Cape Memo", sal_p1_eastern_cape_memo_2008_1),
        ("2008_1 SAL P1 Gauteng", sal_p1_gauteng_2008_1),
        ("2008_1 SAL P1 Gauteng Memo", sal_p1_gauteng_memo_2008_1),
        ("2008_1 SAL P1 Western Cape", sal_p1_western_cape_2008_1),
        ("2008_1 SAL P1 Western Cape Memo", sal_p1_western_cape_memo_2008_1),
        ("2008_1 SAL P2 Memo", sal_p2_memo_2008_1),

        # --- 2009 ---
        ("2009 FAL P1 Memo", fal_p1_2009_memo),
        ("2009 FAL P1 Paper", fal_p1_2009_paper),
        ("2009 FAL P3 Paper", fal_p3_2009_paper),
        ("2009 FAL P3 Rubric", fal_p3_2009_rubric),
        ("2009 HL P1 Paper", hl_p1_2009_paper),
        ("2009 HL P2 Memo", hl_p2_2009_memo),
        ("2009 HL P2 Paper", hl_p2_2009_paper),
        ("2009 HL P3 Paper", hl_p3_2009_paper),
        ("2009 HL P3 Rubric", hl_p3_2009_rubric),
        ("2009 SAL P2 Paper", sal_p2_2009_paper),
        ("2009 SAL P2 Rubric", sal_p2_2009_rubric),
        ("2009 SAL P1 Eastern Cape", sal_p1_2009_eastern_cape),
        ("2009 SAL P1 Western Cape", sal_p1_2009_western_cape),

        # --- 2011 (first sitting) ---
        ("2011 FAL P1 Memo", fal_p1_2011_memo),
        ("2011 FAL P1 Paper", fal_p1_2011_paper),
        ("2011 FAL P2 Memo", fal_p2_2011_memo),
        ("2011 FAL P2 Paper", fal_p2_2011_paper),
        ("2011 FAL P3 Memo", fal_p3_2011_memo),
        ("2011 FAL P3 Paper", fal_p3_2011_paper),
        ("2011 HL P1 Memo", hl_p1_2011_memo),
        ("2011 HL P1 Paper", hl_p1_2011_paper),
        ("2011 HL P2 Memo", hl_p2_2011_memo),
        ("2011 HL P2 Paper", hl_p2_2011_paper),
        ("2011 HL P3 Memo", hl_p3_2011_memo),
        ("2011 HL P3 Paper", hl_p3_2011_paper),
        ("2011 SAL P1 Eastern Cape", sal_p1_2011_eastern_cape),
        ("2011 SAL P2 Memo", sal_p2_2011_memo),
        ("2011 SAL P2 Paper", sal_p2_2011_paper),

        # --- 2011_1 (November) ---
        ("2011_1 FAL P1", fal_p1_2011_1),
        ("2011_1 FAL P2", fal_p2_2011_1),
        ("2011_1 FAL P3", fal_p3_2011_1),
        ("2011_1 HL P1", hl_p1_2011_1),
        ("2011_1 HL P2", hl_p2_2011_1),
        ("2011_1 HL P3", hl_p3_2011_1),
        ("2011_1 SAL P1 Eastern Cape", sal_p1_2011_1_eastern_cape),
        ("2011_1 SAL P1 Western Cape", sal_p1_2011_1_western_cape),
        ("2011_1 SAL P2", sal_p2_2011_1),
    ]

    df = pd.DataFrame(records, columns=["paper_name", "raw_text"])
    return df


# ---------- cleaners ----------
# ---------- cleaners ----------
def clean_raw_text(text: str) -> str:
    # remove isolated numbers (keep things like years in prose if attached to words)
    text = re.sub(r"\b\d+(?:\.\d+)?\b", "", text)
    # drop common header tokens (case-insensitive)
    text = re.sub(r"\b(?:FAL|HL|SAL|P1|P2|P3|MEMO|RUBRIC)\b", "", text, flags=re.IGNORECASE)
    # keep letters, digits, spaces and common punctuation (removed parentheses from allowed chars)
    text = re.sub(r"[^\w\s’\-.,!?]", " ", text)
    # remove leftover isolated () sequences
    text = re.sub(r"\(\s*\)", " ", text)
    # squeeze whitespace
    text = re.sub(r"\s{2,}", " ", text)
    return text.strip()



def split_into_sentences(text: str) -> list[str]:
    # split on sentence-ending punctuation regardless of next char’s case
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [s.strip() for s in parts if len(s.strip()) > 10]


def extract_sentences_node(df: pd.DataFrame) -> pd.DataFrame:
    seen = set()
    clean_sentences = []

    for raw_text in df["raw_text"]:
        cleaned = clean_raw_text(raw_text)
        for sentence in split_into_sentences(cleaned):
            s = sentence.strip().strip('"').strip("'")
            key = s.lower()
            if key not in seen:
                clean_sentences.append(s)
                seen.add(key)

    return pd.DataFrame(clean_sentences, columns=["sentence"])
