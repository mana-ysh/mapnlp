from typing import Iterable

from mapnlp.annotator.base import Annotator
from mapnlp.annotation.base import SequentialAnnotation
from mapnlp.data.chunk import Chunk
from mapnlp.data.morpheme import Morpheme
from mapnlp.data.sentence import Sentence


class SequentialAnnotator(Annotator):
    TYPE = None
    @staticmethod
    def _convert_alg_output(
            alg_output: Iterable[TYPE.__class__.__name__]
    ) -> SequentialAnnotation[TYPE.__class__.__name__]:
        return SequentialAnnotation(alg_output)


class MorphemeSequentialAnnotator(SequentialAnnotator):
    TYPE = Morpheme


class ChunkSequentialAnnotator(SequentialAnnotator):
    TYPE = Chunk


class SentenceSequentialAnnotator(SequentialAnnotator):
    TYPE = Sentence