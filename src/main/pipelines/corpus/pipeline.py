from kedro.pipeline import Pipeline, node
from .nodes import concat_corpora


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=concat_corpora,
                inputs=["isiXhosa_sentences", "bible_text_corpus","combined_data_source_3_texts"],
                outputs="full_text_corpus",
                name="concat_dobe_and_bibles",
            ),
        ]
    )
