"""Project pipelines."""
from __future__ import annotations

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from main.pipelines import DoBE_grade12, corpus_progress, bible, corpus, Data_source_3



def register_pipelines() -> dict[str, Pipeline]:
    return {
        "__default__": DoBE_grade12.create_pipeline(),
        "DoBE_grade12": DoBE_grade12.create_pipeline(),
        "corpus_progress": corpus_progress.create_pipeline(),
        "bible": bible.create_pipeline(),
        "corpus": corpus.create_pipeline(),
        "Data_source_3": Data_source_3.create_pipeline(),
    }