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
        # --- 2012 (Feb-March) ---
    fal_p1_febmarch_memo_2012: str,
    fal_p1_febmarch_paper_2012: str,
    fal_p2_febmarch_memo_2012: str,
    fal_p2_febmarch_paper_2012: str,
    fal_p3_febmarch_memo_2012: str,
    fal_p3_febmarch_paper_2012: str,
    hl_p1_febmarch_memo_2012: str,
    hl_p1_febmarch_paper_2012: str,
    hl_p2_febmarch_paper_2012: str,
    hl_p3_febmarch_memo_2012: str,
    hl_p3_febmarch_paper_2012: str,
    sal_p1_febmarch_easterncape_paper_2012: str,
    sal_p1_febmarch_westerncape_paper_2012: str,
    sal_p2_febmarch_memo_2012: str,
    sal_p2_febmarch_paper_2012: str,

    # --- 2012 (November) ---
    fal_p1_nov_memo_2012: str,
    fal_p1_nov_paper_2012: str,
    fal_p2_nov_memo_2012: str,
    fal_p2_nov_paper_2012: str,
    # fal_p3_nov_memo_2012: str,
    fal_p3_nov_paper_2012: str,
    hl_p1_nov_memo_2012: str,
    hl_p1_nov_paper_2012: str,
    hl_p2_nov_memo_2012: str,
    hl_p2_nov_paper_2012: str,
    hl_p3_nov_memo_2012: str,
    hl_p3_nov_paper_2012: str,
    sal_p1_nov_easterncape_paper_2012: str,
    sal_p1_nov_westerncape_paper_2012: str,
    sal_p2_nov_memo_2012: str,
    sal_p2_nov_paper_2012: str,

        # --- 2013 ---
    fal_p3_nov_memo_2013: str,
    fal_p2_feb_march_2013: str,
    hl_p2_feb_march_memo_2013: str,
    hl_p2_feb_march_2013: str,
    hl_p3_feb_march_2013: str,
    hl_p3_feb_march_memo_2013: str,

    # --- 2014 ---
    fal_p2_nov_memo_2014: str,
    fal_p1_feb_march_memo_2014: str,
    fal_p1_feb_march_2014: str,
    fal_p2_feb_march_memo_2014: str,
    fal_p2_feb_march_2014: str,
    fal_p3_feb_march_memo_2014: str,
    fal_p3_feb_march_2014: str,
    hl_p1_feb_march_memo_2014: str,
    hl_p1_feb_march_2014: str,
    hl_p2_feb_march_2014: str,
    hl_p3_feb_march_memo_2014: str,
    hl_p3_feb_march_2014: str,
    sal_p1_feb_march_memo_western_cape_2014: str,
    sal_p1_feb_march_western_cape_2014: str,
    sal_p2_feb_march_memo_2014: str,
    sal_p2_feb_march_2014: str,

    # ---- 2015 ---
    fal_p1_2015: str,
    fal_p1_memo_2015: str,
    fal_p2_2015: str,
    fal_p2_memo_2015: str,
    fal_p3_2015: str,
    fal_p3_memo_2015: str,
    hl_p1_2015: str,
    hl_p1_memo_2015: str,
    hl_p2_2015: str,
    hl_p2_memo_2015: str,
    hl_p3_2015: str,
    hl_p3_memo_2015: str,

    # -- 2015 NOV
    fal_p1_nov_2015: str,
    fal_p1_nov_memo_2015: str,
    fal_p2_nov_2015: str,
    fal_p2_nov_memo_2015: str,
    fal_p3_nov_2015: str,
    fal_p3_nov_memo_2015: str,
    hl_p1_nov_2015: str,
    hl_p1_nov_memo_2015: str,
    hl_p2_nov_2015: str,
    hl_p2_nov_memo_2015: str,
    hl_p3_nov_2015: str,
    hl_p3_nov_memo_2015: str,

    # -- 2016 FEB/MAR
    fal_p1_2016: str,
    fal_p1_memo_2016: str,
    fal_p2_2016: str,
    fal_p2_memo_2016: str,
    fal_p3_2016: str,
    fal_p3_memo_2016: str,
    hl_p1_2016: str,
    hl_p1_memo_2016: str,
    hl_p2_2016: str,
    hl_p2_memo_2016: str,
    hl_p3_2016: str,
    hl_p3_memo_2016: str,


    # -- 2016 NOV
    fal_p1_nov_2016: str,
    fal_p1_nov_memo_2016: str,
    fal_p2_nov_2016: str,
    fal_p2_nov_memo_2016: str,
    fal_p3_nov_2016: str,
    fal_p3_nov_memo_2016: str,
    hl_p1_nov_2016: str,
    hl_p1_nov_memo_2016: str,
    hl_p2_nov_2016: str,
    hl_p2_nov_memo_2016: str,
    hl_p3_nov_2016: str,
    hl_p3_nov_memo_2016: str,


    # -- 2016 OTHER
    fal_p1_other_2016: str,
    fal_p1_other_memo_2016: str,
    fal_p2_other_2016: str,
    fal_p2_other_memo_2016: str,
    fal_p3_other_2016: str,
    fal_p3_other_memo_2016: str,
    hl_p1_other_2016: str,
    hl_p1_other_memo_2016: str,
    hl_p2_other_2016: str,
    hl_p2_other_memo_2016: str,
    hl_p3_other_2016: str,
    hl_p3_other_memo_2016: str,

    # -- 2017 FEB/MAR
    fal_p1_2017: str,
    fal_p1_memo_2017: str,
    fal_p2_2017: str,
    fal_p2_memo_2017: str,
    fal_p3_2017: str,
    fal_p3_memo_2017: str,
    hl_p1_2017: str,
    hl_p1_memo_2017: str,
    hl_p2_2017: str,
    hl_p2_memo_2017: str,
    hl_p3_2017: str,
    hl_p3_memo_2017: str,

    #-- 2017 NOV
    fal_p1_nov_2017: str,
    fal_p1_nov_memo_2017: str,
    fal_p2_nov_2017: str,
    fal_p2_nov_memo_2017: str,
    fal_p3_nov_2017: str,
    fal_p3_nov_memo_2017: str,
    hl_p1_nov_2017: str,
    hl_p1_nov_memo_2017: str,
    # hl_p2_nov_2017: str,
    hl_p2_nov_memo_2017: str,
    hl_p3_nov_2017: str,
    hl_p3_nov_memo_2017: str,

    #-- 2017 OTHER
    fal_p1_other_2017: str,
    fal_p1_other_memo_2017: str,
    fal_p2_other_2017: str,
    fal_p2_other_memo_2017: str,
    fal_p3_other_2017: str,
    fal_p3_other_memo_2017: str,
    hl_p1_other_2017: str,
    hl_p1_other_memo_2017: str,
    hl_p2_other_2017: str,
    hl_p2_other_memo_2017: str,
    hl_p3_other_2017: str,
    hl_p3_other_memo_2017: str,

    # -- 2018 FEB/MAR
    fal_p1_2018: str,
    fal_p1_memo_2018: str,
    fal_p2_2018: str,
    fal_p2_memo_2018: str,
    fal_p3_2018: str,
    fal_p3_memo_2018: str,
    hl_p1_2018: str,
    hl_p1_memo_2018: str,
    hl_p2_2018: str,
    hl_p2_memo_2018: str,
    hl_p3_2018: str,
    hl_p3_memo_2018: str,


     # -- 2018 NOV
    fal_p1_nov_2018: str,
    fal_p1_nov_memo_2018: str,
    fal_p2_nov_2018: str,
    fal_p2_nov_memo_2018: str,
    fal_p3_nov_2018: str,
    fal_p3_nov_memo_2018: str,
    hl_p1_nov_2018: str,
    hl_p1_nov_memo_2018: str,
    hl_p2_nov_2018: str,
    hl_p2_nov_memo_2018: str,
    hl_p3_nov_2018: str,
    hl_p3_nov_memo_2018: str,


    # -- 2018 OTHER
    fal_p1_other_2018: str,
    fal_p1_other_memo_2018: str,
    fal_p2_other_2018: str,
    fal_p2_other_memo_2018: str,
    fal_p3_other_2018: str,
    fal_p3_other_memo_2018: str,
    hl_p1_other_2018: str,
    hl_p1_other_memo_2018: str,
    hl_p2_other_2018: str,
    hl_p2_other_memo_2018: str,
    hl_p3_other_2018: str,
    hl_p3_other_memo_2018: str,


    # --2019 FEB/MAR
    fal_p1_2019: str,
    fal_p1_memo_2019: str,
    fal_p2_2019: str,
    fal_p2_memo_2019: str,
    fal_p3_2019: str,
    fal_p3_memo_2019: str,
    hl_p1_2019: str,
    hl_p1_memo_2019: str,
    hl_p2_2019: str,
    hl_p2_memo_2019: str,
    hl_p3_2019: str,
    hl_p3_memo_2019: str,


    # --2019 NOV
    fal_p1_nov_2019: str,
    fal_p1_nov_memo_2019: str,
    fal_p2_nov_2019: str,
    fal_p2_nov_memo_2019: str,
    fal_p3_nov_2019: str,
    fal_p3_nov_memo_2019: str,
    hl_p1_nov_2019: str,
    hl_p1_nov_memo_2019: str,
    hl_p2_nov_2019: str,
    hl_p2_nov_memo_2019: str,
    hl_p3_nov_2019: str,
    hl_p3_nov_memo_2019: str,
    sal_p1_nov_2019: str,
    sal_p1_nov_memo_2019: str,
    sal_p2_nov_2019: str,
    sal_p2_nov_memo_2019: str,



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

                # --- 2012 (Feb-March) ---
        ("2012 FAL P1 Feb-March Memo", fal_p1_febmarch_memo_2012),
        ("2012 FAL P1 Feb-March Paper", fal_p1_febmarch_paper_2012),
        ("2012 FAL P2 Feb-March Memo", fal_p2_febmarch_memo_2012),
        ("2012 FAL P2 Feb-March Paper", fal_p2_febmarch_paper_2012),
        ("2012 FAL P3 Feb-March Memo", fal_p3_febmarch_memo_2012),
        ("2012 FAL P3 Feb-March Paper", fal_p3_febmarch_paper_2012),
        ("2012 HL P1 Feb-March Memo", hl_p1_febmarch_memo_2012),
        ("2012 HL P1 Feb-March Paper", hl_p1_febmarch_paper_2012),
        ("2012 HL P2 Feb-March Paper", hl_p2_febmarch_paper_2012),
        ("2012 HL P3 Feb-March Memo", hl_p3_febmarch_memo_2012),
        ("2012 HL P3 Feb-March Paper", hl_p3_febmarch_paper_2012),
        ("2012 SAL P1 Feb-March Eastern Cape Paper", sal_p1_febmarch_easterncape_paper_2012),
        ("2012 SAL P1 Feb-March Western Cape Paper", sal_p1_febmarch_westerncape_paper_2012),
        ("2012 SAL P2 Feb-March Memo", sal_p2_febmarch_memo_2012),
        ("2012 SAL P2 Feb-March Paper", sal_p2_febmarch_paper_2012),

        # --- 2012 (November) ---
        ("2012 FAL P1 Nov Memo", fal_p1_nov_memo_2012),
        ("2012 FAL P1 Nov Paper", fal_p1_nov_paper_2012),
        ("2012 FAL P2 Nov Memo", fal_p2_nov_memo_2012),
        ("2012 FAL P2 Nov Paper", fal_p2_nov_paper_2012),
        # ("2012 FAL P3 Nov Memo", fal_p3_nov_memo_2012),
        ("2012 FAL P3 Nov Paper", fal_p3_nov_paper_2012),
        ("2012 HL P1 Nov Memo", hl_p1_nov_memo_2012),
        ("2012 HL P1 Nov Paper", hl_p1_nov_paper_2012),
        ("2012 HL P2 Nov Memo", hl_p2_nov_memo_2012),
        ("2012 HL P2 Nov Paper", hl_p2_nov_paper_2012),
        ("2012 HL P3 Nov Memo", hl_p3_nov_memo_2012),
        ("2012 HL P3 Nov Paper", hl_p3_nov_paper_2012),
        ("2012 SAL P1 Nov Eastern Cape Paper", sal_p1_nov_easterncape_paper_2012),
        ("2012 SAL P1 Nov Western Cape Paper", sal_p1_nov_westerncape_paper_2012),
        ("2012 SAL P2 Nov Memo", sal_p2_nov_memo_2012),
        ("2012 SAL P2 Nov Paper", sal_p2_nov_paper_2012),

        # --- 2013 ---
        ("2013 FAL P3 Nov Memo", fal_p3_nov_memo_2013),
        ("2013 FAL P1 Feb-March", fal_p2_feb_march_2013),
        ("2013 HL P2 Feb-March Memo", hl_p2_feb_march_memo_2013),
        ("2013 HL P2 Feb-March", hl_p2_feb_march_2013),
        ("2013 HL P3 Feb-March", hl_p3_feb_march_2013),
        ("2013 HL P3 Feb-March Memo", hl_p3_feb_march_memo_2013),

        # --- 2014 ---
        ("2014 FAL P2 Nov Memo", fal_p2_nov_memo_2014),
        ("2014 FAL P1 Feb-March Memo", fal_p1_feb_march_memo_2014),
        ("2014 FAL P1 Feb-March", fal_p1_feb_march_2014),
        ("2014 FAL P2 Feb-March Memo", fal_p2_feb_march_memo_2014),
        ("2014 FAL P2 Feb-March", fal_p2_feb_march_2014),
        ("2014 FAL P3 Feb-March Memo", fal_p3_feb_march_memo_2014),
        ("2014 FAL P3 Feb-March", fal_p3_feb_march_2014),
        ("2014 HL P1 Feb-March Memo", hl_p1_feb_march_memo_2014),
        ("2014 HL P1 Feb-March", hl_p1_feb_march_2014),
        ("2014 HL P2 Feb-March", hl_p2_feb_march_2014),
        ("2014 HL P3 Feb-March Memo", hl_p3_feb_march_memo_2014),
        ("2014 HL P3 Feb-March", hl_p3_feb_march_2014),
        ("2014 SAL P1 Feb-March Memo (Western Cape)", sal_p1_feb_march_memo_western_cape_2014),
        ("2014 SAL P1 Feb-March (Western Cape)", sal_p1_feb_march_western_cape_2014),
        ("2014 SAL P2 Feb-March Memo", sal_p2_feb_march_memo_2014),
        ("2014 SAL P2 Feb-March", sal_p2_feb_march_2014),

        # --- 2015 ---
       ("2015 FAL P1", fal_p1_2015),
       ("2015 FAL P1 Memo", fal_p1_memo_2015),
       ("2015 FAL P2", fal_p2_2015),
       ("2015 FAL P2 Memo", fal_p2_memo_2015),
       ("2015 FAL P3", fal_p3_2015),
       ("2015 FAL P3 Memo", fal_p3_memo_2015),
       ("2015 HL P1", hl_p1_2015),
       ("2015 HL P1 Memo", hl_p1_memo_2015),
       ("2015 HL P2", hl_p2_2015),
       ("2015 HL P2 Memo", hl_p2_memo_2015),
       ("2015 HL P3", hl_p3_2015),
       ("2015 HL P3 Memo", hl_p3_memo_2015),

       #--- 2015 NOV --    
       ("2015 Nov FAL P1", fal_p1_nov_2015),
       ("2015 Nov FAL P1 Memo", fal_p1_nov_memo_2015),
       ("2015 Nov FAL P2", fal_p2_nov_2015),
       ("2015 Nov FAL P2 Memo", fal_p2_nov_memo_2015),
       ("2015 Nov FAL P3", fal_p3_nov_2015),
       ("2015 Nov FAL P3 Memo", fal_p3_nov_memo_2015),
       ("2015 Nov HL P1", hl_p1_nov_2015),
       ("2015 Nov HL P1 Memo", hl_p1_nov_memo_2015),
       ("2015 Nov HL P2", hl_p2_nov_2015),
       ("2015 Nov HL P2 Memo", hl_p2_nov_memo_2015),
       ("2015 Nov HL P3", hl_p3_nov_2015),
       ("2015 Nov HL P3 Memo", hl_p3_nov_memo_2015),


       # -- 2016 FEB/MAR ---   
        ("2016 FAL P1", fal_p1_2016),
        ("2016 FAL P1 Memo", fal_p1_memo_2016),
        ("2016 FAL P2", fal_p2_2016),
        ("2016 FAL P2 Memo", fal_p2_memo_2016),
        ("2016 FAL P3", fal_p3_2016),
        ("2016 FAL P3 Memo", fal_p3_memo_2016),
        ("2016 HL P1", hl_p1_2016),
        ("2016 HL P1 Memo", hl_p1_memo_2016),
        ("2016 HL P2", hl_p2_2016),
        ("2016 HL P2 Memo", hl_p2_memo_2016),
        ("2016 HL P3", hl_p3_2016),
        ("2016 HL P3 Memo", hl_p3_memo_2016),


        # -- 2016 NOV ---
        ("2016 Nov FAL P1", fal_p1_nov_2016),
        ("2016 Nov FAL P1 Memo", fal_p1_nov_memo_2016),
        ("2016 Nov FAL P2", fal_p2_nov_2016),
        ("2016 Nov FAL P2 Memo", fal_p2_nov_memo_2016),
        ("2016 Nov FAL P3", fal_p3_nov_2016),
        ("2016 Nov FAL P3 Memo", fal_p3_nov_memo_2016),
        ("2016 Nov HL P1", hl_p1_nov_2016),
        ("2016 Nov HL P1 Memo", hl_p1_nov_memo_2016),
        ("2016 Nov HL P2", hl_p2_nov_2016),
        ("2016 Nov HL P2 Memo", hl_p2_nov_memo_2016),
        ("2016 Nov HL P3", hl_p3_nov_2016),
        ("2016 Nov HL P3 Memo", hl_p3_nov_memo_2016),

        # -- 2016 OTHER ---
        ("2016 Other FAL P1", fal_p1_other_2016),
        ("2016 Other FAL P1 Memo", fal_p1_other_memo_2016),
        ("2016 Other FAL P2", fal_p2_other_2016),
        ("2016 Other FAL P2 Memo", fal_p2_other_memo_2016),
        ("2016 Other FAL P3", fal_p3_other_2016),
        ("2016 Other FAL P3 Memo", fal_p3_other_memo_2016),
        ("2016 Other HL P1", hl_p1_other_2016),
        ("2016 Other HL P1 Memo", hl_p1_other_memo_2016),
        ("2016 Other HL P2", hl_p2_other_2016),
        ("2016 Other HL P2 Memo", hl_p2_other_memo_2016),
        ("2016 Other HL P3", hl_p3_other_2016),
        ("2016 Other HL P3 Memo", hl_p3_other_memo_2016),

        # -- 2017 FEB/MAR ---
        ("2017 FAL P1", fal_p1_2017),
        ("2017 FAL P1 Memo", fal_p1_memo_2017),
        ("2017 FAL P2", fal_p2_2017),
        ("2017 FAL P2 Memo", fal_p2_memo_2017),
        ("2017 FAL P3", fal_p3_2017),
        ("2017 FAL P3 Memo", fal_p3_memo_2017),
        ("2017 HL P1", hl_p1_2017),
        ("2017 HL P1 Memo", hl_p1_memo_2017),
        ("2017 HL P2", hl_p2_2017),
        ("2017 HL P2 Memo", hl_p2_memo_2017),
        ("2017 HL P3", hl_p3_2017),
        ("2017 HL P3 Memo", hl_p3_memo_2017),

        # 2017 NOV
        ("2017 Nov FAL P1", fal_p1_nov_2017),
        ("2017 Nov FAL P1 Memo", fal_p1_nov_memo_2017),
        ("2017 Nov FAL P2", fal_p2_nov_2017),
        ("2017 Nov FAL P2 Memo", fal_p2_nov_memo_2017),
        ("2017 Nov FAL P3", fal_p3_nov_2017),
        ("2017 Nov FAL P3 Memo", fal_p3_nov_memo_2017),
        ("2017 Nov HL P1", hl_p1_nov_2017),
        ("2017 Nov HL P1 Memo", hl_p1_nov_memo_2017),
        # ("2017 Nov HL P2", hl_p2_nov_2017),
        ("2017 Nov HL P2 Memo", hl_p2_nov_memo_2017),
        ("2017 Nov HL P3", hl_p3_nov_2017),
        ("2017 Nov HL P3 Memo", hl_p3_nov_memo_2017),

        # 2017 OTHER
        ("2017 Other FAL P1", fal_p1_other_2017),
        ("2017 Other FAL P1 Memo", fal_p1_other_memo_2017),
        ("2017 Other FAL P2", fal_p2_other_2017),
        ("2017 Other FAL P2 Memo", fal_p2_other_memo_2017),
        ("2017 Other FAL P3", fal_p3_other_2017),
        ("2017 Other FAL P3 Memo", fal_p3_other_memo_2017),
        ("2017 Other HL P1", hl_p1_other_2017),
        ("2017 Other HL P1 Memo", hl_p1_other_memo_2017),
        ("2017 Other HL P2", hl_p2_other_2017),
        ("2017 Other HL P2 Memo", hl_p2_other_memo_2017),
        ("2017 Other HL P3", hl_p3_other_2017),
        ("2017 Other HL P3 Memo", hl_p3_other_memo_2017),

        # 2018 FEB/MAR
        ("2018 FAL P1", fal_p1_2018),
        ("2018 FAL P1 Memo", fal_p1_memo_2018),
        ("2018 FAL P2", fal_p2_2018),
        ("2018 FAL P2 Memo", fal_p2_memo_2018),
        ("2018 FAL P3", fal_p3_2018),
        ("2018 FAL P3 Memo", fal_p3_memo_2018),
        ("2018 HL P1", hl_p1_2018),
        ("2018 HL P1 Memo", hl_p1_memo_2018),
        ("2018 HL P2", hl_p2_2018),
        ("2018 HL P2 Memo", hl_p2_memo_2018),
        ("2018 HL P3", hl_p3_2018),
        ("2018 HL P3 Memo", hl_p3_memo_2018),

        # 2018 NOV
        ("2018 Nov FAL P1", fal_p1_nov_2018),
        ("2018 Nov FAL P1 Memo", fal_p1_nov_memo_2018),
        ("2018 Nov FAL P2", fal_p2_nov_2018),
        ("2018 Nov FAL P2 Memo", fal_p2_nov_memo_2018),
        ("2018 Nov FAL P3", fal_p3_nov_2018),
        ("2018 Nov FAL P3 Memo", fal_p3_nov_memo_2018),
        ("2018 Nov HL P1", hl_p1_nov_2018),
        ("2018 Nov HL P1 Memo", hl_p1_nov_memo_2018),
        ("2018 Nov HL P2", hl_p2_nov_2018),
        ("2018 Nov HL P2 Memo", hl_p2_nov_memo_2018),
        ("2018 Nov HL P3", hl_p3_nov_2018),
        ("2018 Nov HL P3 Memo", hl_p3_nov_memo_2018),


        # 2018 OTHER
        ("2018 Other FAL P1", fal_p1_other_2018),
        ("2018 Other FAL P1 Memo", fal_p1_other_memo_2018),
        ("2018 Other FAL P2", fal_p2_other_2018),
        ("2018 Other FAL P2 Memo", fal_p2_other_memo_2018),
        ("2018 Other FAL P3", fal_p3_other_2018),
        ("2018 Other FAL P3 Memo", fal_p3_other_memo_2018),
        ("2018 Other HL P1", hl_p1_other_2018),
        ("2018 Other HL P1 Memo", hl_p1_other_memo_2018),
        ("2018 Other HL P2", hl_p2_other_2018),
        ("2018 Other HL P2 Memo", hl_p2_other_memo_2018),
        ("2018 Other HL P3", hl_p3_other_2018),
        ("2018 Other HL P3 Memo", hl_p3_other_memo_2018),

        # 2019 FEB/MAR
        ("2019 FAL P1", fal_p1_2019),
        ("2019 FAL P1 Memo", fal_p1_memo_2019),
        ("2019 FAL P2", fal_p2_2019),
        ("2019 FAL P2 Memo", fal_p2_memo_2019),
        ("2019 FAL P3", fal_p3_2019),
        ("2019 FAL P3 Memo", fal_p3_memo_2019),
        ("2019 HL P1", hl_p1_2019),
        ("2019 HL P1 Memo", hl_p1_memo_2019),
        ("2019 HL P2", hl_p2_2019),
        ("2019 HL P2 Memo", hl_p2_memo_2019),
        ("2019 HL P3", hl_p3_2019),
        ("2019 HL P3 Memo", hl_p3_memo_2019),


        ("2019 Nov FAL P1", fal_p1_nov_2019),
        ("2019 Nov FAL P1 Memo", fal_p1_nov_memo_2019),
        ("2019 Nov FAL P2", fal_p2_nov_2019),
        ("2019 Nov FAL P2 Memo", fal_p2_nov_memo_2019),
        ("2019 Nov FAL P3", fal_p3_nov_2019),
        ("2019 Nov FAL P3 Memo", fal_p3_nov_memo_2019),

        ("2019 Nov HL P1", hl_p1_nov_2019),
        ("2019 Nov HL P1 Memo", hl_p1_nov_memo_2019),
        ("2019 Nov HL P2", hl_p2_nov_2019),
        ("2019 Nov HL P2 Memo", hl_p2_nov_memo_2019),
        ("2019 Nov HL P3", hl_p3_nov_2019),
        ("2019 Nov HL P3 Memo", hl_p3_nov_memo_2019),

        ("2019 Nov SAL P1", sal_p1_nov_2019),
        ("2019 Nov SAL P1 Memo", sal_p1_nov_memo_2019),
        ("2019 Nov SAL P2", sal_p2_nov_2019),
        ("2019 Nov SAL P2 Memo", sal_p2_nov_memo_2019),


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
