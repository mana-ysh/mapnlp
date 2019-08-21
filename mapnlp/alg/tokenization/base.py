
from typing import List

from mapnlp.annotator.sequential import MorphemeSequentialAnnotator
from mapnlp.alg.base import Algorithm, AlgorithmFactory
from mapnlp.data.morpheme import Morpheme


class Tokenizer(Algorithm, MorphemeSequentialAnnotator):
    TASK_NAME = "tokenizer"

    def run(self, _input: str) -> List[Morpheme]:
        raise NotImplementedError()


class TokenizerFactory(AlgorithmFactory):
    NAME2CLASS = Tokenizer.ALGORITHM_POOL[Tokenizer.TASK_NAME]