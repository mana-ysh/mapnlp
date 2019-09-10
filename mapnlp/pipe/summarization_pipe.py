
from mapnlp.alg.summarization import TextSummarizerFactory
from mapnlp.annotation_extractor.morph_seq_extractor import MorphSequenceSeriesExtractor
from mapnlp.pipe.base import NLPPipe


class TextSummarizerPipe(NLPPipe):
    DEFAULT_ANNOTATION_EXTRACTOR = MorphSequenceSeriesExtractor()
    DEFAULT_ALGORITHM_NAME = "lead"
    ALGORITHM_FACTORY_CLASS = TextSummarizerFactory
