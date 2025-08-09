from kedro.pipeline import Pipeline, node, pipeline
from .nodes import corpus_progress_node

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=corpus_progress_node,
            inputs=dict(
                corpus_root="params:corpus_progress.corpus_root",
                file_glob="params:corpus_progress.file_glob",
                dedup="params:corpus_progress.dedup",
                min_doc_chars="params:corpus_progress.min_doc_chars",
                report_title="params:corpus_progress.report_title",
                text_column="params:corpus_progress.text_column",  # NEW
            ),
            outputs=[
                "corpus_progress_files_table",
                "corpus_progress_milestones_table",
                "corpus_progress_report_md"
            ],
            name="corpus_progress_node",
        )
    ])
