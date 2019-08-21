
from typing import List

from mapnlp.annotator.sequential import ChunkSequentialAnnotator
from mapnlp.alg.base import Algorithm, AlgorithmFactory
from mapnlp.data.chunk import Chunk
from mapnlp.data.morpheme import Morpheme


class Chunker(Algorithm, ChunkSequentialAnnotator):
    TASK_NAME = "chunker"

    def run(self, _input: List[Morpheme]) -> List[Chunk]:
        raise NotImplementedError()


class ChunkerFactory(AlgorithmFactory):
    NAME2CLASS = Chunker.ALGORITHM_POOL[Chunker.TASK_NAME]