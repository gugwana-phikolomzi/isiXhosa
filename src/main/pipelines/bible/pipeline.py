from kedro.pipeline import Pipeline, node
from .nodes import select_and_concat_textframes

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func=select_and_concat_textframes,
            inputs=["xho75", "xho96", "xho1902a"],
            outputs="bible_text_corpus",
            name="concat_bible_texts",
        ),
    ])
