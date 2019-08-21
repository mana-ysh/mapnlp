
from typing import Any

from mapnlp.data.base import InputText


class AnnotationExtractor:
    def __init__(self):
        pass

    def extract(self, input_text: InputText) -> Any:
        """
        For transferring input data from NLPPipe to Algorithm
        """
        raise NotImplementedError()


class OriginalTextExtractor(AnnotationExtractor):
    def extract(self, input_text: InputText) -> str:
        return input_text.original_text
