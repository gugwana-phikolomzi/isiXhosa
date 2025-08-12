from kedro.pipeline import Pipeline, node, pipeline
from .nodes import combine_texts

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=combine_texts,
                inputs=["entsimini", "ezemidlalo", "ezoyolo"],
                outputs="combined_data_source_3_texts",
                name="combine_data_source_3_texts",
            ),
        ]
    )
