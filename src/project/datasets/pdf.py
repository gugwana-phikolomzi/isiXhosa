
from kedro.io import AbstractDataSet
from PyPDF2 import PdfReader

class PDFTextDataSet(AbstractDataSet):
    def __init__(self, filepath: str):
        self._filepath = filepath

    def _load(self) -> str:
        reader = PdfReader(self._filepath)
        return "\n".join(page.extract_text() for page in reader.pages)

    def _save(self, data: str) -> None:
        raise NotImplementedError("This dataset is read-only.")

    def _describe(self):
        return dict(filepath=self._filepath)
