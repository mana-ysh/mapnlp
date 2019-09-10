
from typing import List

from mapnlp.annotator.text import TextAnnotator
from mapnlp.alg.base import Algorithm, AlgorithmFactory
from mapnlp.data.base import SpanTextUnit
from mapnlp.data.sentence import Sentence


class TextSummarizer(Algorithm, TextAnnotator):
    """
    simple text summarizer, which output flat text
    """
    TASK_NAME = "text-summarization"

    def run(self, _input: List[List[SpanTextUnit]]) -> str:
        raise NotImplementedError()


# TODO: implement Annotator
class SentenceExtractiveSummarizer(Algorithm):
    """
    sentence extractive summarizer, which output the indicator for each sentence
    """
    TASK_NAME = "sentence-extractive-summarization"

    def run(self, _input: List[Sentence]) -> List[bool]:
        raise NotImplementedError()


class TextSummarizerFactory(AlgorithmFactory):
    NAME2CLASS = TextSummarizer.ALGORITHM_POOL[TextSummarizer.TASK_NAME]


class SentenceExtractiveSummarizerFactory(AlgorithmFactory):
    NAME2CLASS = SentenceExtractiveSummarizer.ALGORITHM_POOL[SentenceExtractiveSummarizer.TASK_NAME]


