
from typing import List

from mapnlp.annotator.sequential import SentenceSequentialAnnotator
from mapnlp.alg.base import Algorithm, AlgorithmFactory
from mapnlp.data.sentence import Sentence


class SentenceSplitter(Algorithm, SentenceSequentialAnnotator):
    TASK_NAME = "sentence-splitter"

    def run(self, _input: str) -> List[Sentence]:
        raise NotImplementedError()


class SentenceSplitterFactory(AlgorithmFactory):
    NAME2CLASS = SentenceSplitter.ALGORITHM_POOL[SentenceSplitter.TASK_NAME]
