from kedro.pipeline import Pipeline, node, pipeline
from .nodes import clean_exam_data, extract_sentences_node

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=clean_exam_data,
                inputs={
                    # --- 2008 ---
                    "fal_p1": "raw_2008_fal_p1",
                    "fal_p1_memo": "raw_2008_fal_p1_memo",
                    "fal_p3": "raw_2008_fal_p3",
                    "hl_p1": "raw_2008_hl_p1",
                    "hl_p1_memo": "raw_2008_hl_p1_memo",
                    "hl_p3": "raw_2008_hl_p3",
                    "sal_p1_eastern_cape": "raw_2008_sal_p1_eastern_cape",
                    "sal_p1_eastern_cape_memo": "raw_2008_sal_p1_eastern_cape_memo",
                    "sal_p1_gauteng": "raw_2008_sal_p1_gauteng",
                    "sal_p1_gauteng_memo": "raw_2008_sal_p1_gauteng_memo",
                    "sal_p1_western_cape": "raw_2008_sal_p1_western_cape",
                    "sal_p1_western_cape_memo": "raw_2008_sal_p1_western_cape_memo",
                    "sal_p2_memo": "raw_2008_sal_p2_memo",

                    # --- 2008_1 (Nov 2008) ---
                    "fal_p1_2008_1": "raw_2008_1_fal_p1",
                    "fal_p1_memo_2008_1": "raw_2008_1_fal_p1_memo",
                    "fal_p3_2008_1": "raw_2008_1_fal_p3",
                    "hl_p1_2008_1": "raw_2008_1_hl_p1",
                    "hl_p1_memo_2008_1": "raw_2008_1_hl_p1_memo",
                    "hl_p3_2008_1": "raw_2008_1_hl_p3",
                    "sal_p1_eastern_cape_2008_1": "raw_2008_1_sal_p1_eastern_cape",
                    "sal_p1_eastern_cape_memo_2008_1": "raw_2008_1_sal_p1_eastern_cape_memo",
                    "sal_p1_gauteng_2008_1": "raw_2008_1_sal_p1_gauteng",
                    "sal_p1_gauteng_memo_2008_1": "raw_2008_1_sal_p1_gauteng_memo",
                    "sal_p1_western_cape_2008_1": "raw_2008_1_sal_p1_western_cape",
                    "sal_p1_western_cape_memo_2008_1": "raw_2008_1_sal_p1_western_cape_memo",
                    "sal_p2_memo_2008_1": "raw_2008_1_sal_p2_memo",

                    # --- 2009 ---
                    "fal_p1_2009_memo":   "raw_2009_isixhosa_fal_p1_nov_memo_pdf",
                    "fal_p1_2009_paper":  "raw_2009_isixhosa_fal_p1_nov_paper_pdf",
                    "fal_p3_2009_paper":  "raw_2009_isixhosa_fal_p3_nov_paper_pdf",
                    "fal_p3_2009_rubric": "raw_2009_isixhosa_fal_p3_nov_rubric_pdf",
                    "hl_p1_2009_paper":   "raw_2009_isixhosa_hl_p1_nov_paper_pdf",
                    "hl_p2_2009_memo":    "raw_2009_isixhosa_hl_p2_nov_memo_pdf",
                    "hl_p2_2009_paper":   "raw_2009_isixhosa_hl_p2_nov_paper_pdf",
                    "hl_p3_2009_paper":   "raw_2009_isixhosa_hl_p3_nov_paper_pdf",
                    "hl_p3_2009_rubric":  "raw_2009_isixhosa_hl_p3_nov_rubric_pdf",
                    "sal_p2_2009_paper":  "raw_2009_isixhosa_sal_p2_nov_paper_pdf",
                    "sal_p2_2009_rubric": "raw_2009_isixhosa_sal_p2_nov_rubric_pdf",
                    "sal_p1_2009_eastern_cape": "raw_2009_isixhosa_sal_p1_nov_eastern_cape_pdf",
                    "sal_p1_2009_western_cape": "raw_2009_isixhosa_sal_p1_nov_western_cape_pdf",

                    # --- 2011 ---
                    "fal_p1_2011_memo":   "raw_2011_isixhosa_fal_p1_memo_pdf",
                    "fal_p1_2011_paper":  "raw_2011_isixhosa_fal_p1_pdf",
                    "fal_p2_2011_memo":   "raw_2011_isixhosa_fal_p2_memo_pdf",
                    "fal_p2_2011_paper":  "raw_2011_isixhosa_fal_p2_pdf",
                    "fal_p3_2011_memo":   "raw_2011_isixhosa_fal_p3_memo_pdf",
                    "fal_p3_2011_paper":  "raw_2011_isixhosa_fal_p3_pdf",
                    "hl_p1_2011_memo":    "raw_2011_isixhosa_hl_p1_memo_pdf",
                    "hl_p1_2011_paper":   "raw_2011_isixhosa_hl_p1_pdf",
                    "hl_p2_2011_memo":    "raw_2011_isixhosa_hl_p2_memo_pdf",
                    "hl_p2_2011_paper":   "raw_2011_isixhosa_hl_p2_pdf",
                    "hl_p3_2011_memo":    "raw_2011_isixhosa_hl_p3_memo_pdf",
                    "hl_p3_2011_paper":   "raw_2011_isixhosa_hl_p3_pdf",
                    "sal_p1_2011_eastern_cape": "raw_2011_isixhosa_sal_p1_eastern_cape_pdf",
                    "sal_p2_2011_memo":   "raw_2011_isixhosa_sal_p2_memo_pdf",
                    "sal_p2_2011_paper":  "raw_2011_isixhosa_sal_p2_pdf",

                    # --- 2011_1 ---
                    "fal_p1_2011_1":  "raw_2011_isixhosa_fal_p1_nov_pdf",
                    "fal_p2_2011_1":  "raw_2011_isixhosa_fal_p2_nov_pdf",
                    "fal_p3_2011_1":  "raw_2011_isixhosa_fal_p3_nov_pdf",
                    "hl_p1_2011_1":   "raw_2011_isixhosa_hl_p1_nov_pdf",
                    "hl_p2_2011_1":   "raw_2011_isixhosa_hl_p2_nov_pdf",
                    "hl_p3_2011_1":   "raw_2011_isixhosa_hl_p3_nov_pdf",
                    "sal_p1_2011_1_eastern_cape": "raw_2011_isixhosa_sal_p1_eastern_cape_nov_pdf",
                    "sal_p1_2011_1_western_cape": "raw_2011_isixhosa_sal_p1_western_cape_nov_pdf",
                    "sal_p2_2011_1":  "raw_2011_isixhosa_sal_p2_nov_pdf",



                },
                outputs="cleaned_grade12_exam_data",
                name="clean_exam_data_node",
            ),
            node(
                func=extract_sentences_node,
                inputs="cleaned_grade12_exam_data",
                outputs="isiXhosa_sentences",
                name="extract_sentences_node",
            ),
        ]
    )
