"""Project pipelines."""
from __future__ import annotations

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from main.pipelines import DoBE_grade12
from main.pipelines import corpus_progress



def register_pipelines() -> dict[str, Pipeline]:
    return {
        "__default__": DoBE_grade12.create_pipeline(),
        "DoBE_grade12": DoBE_grade12.create_pipeline(),
        "corpus_progress": corpus_progress.create_pipeline(),
    }