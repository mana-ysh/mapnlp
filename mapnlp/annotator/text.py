from mapnlp.annotation.base import TextAnnotation
from mapnlp.annotator.base import Annotator


class TextAnnotator(Annotator):
    @staticmethod
    def _convert_alg_output(alg_output: str) -> TextAnnotation:
        return TextAnnotation(alg_output)
