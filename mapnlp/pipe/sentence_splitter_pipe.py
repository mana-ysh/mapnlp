
from mapnlp.alg.sentence_splitter import SentenceSplitterFactory
from mapnlp.annotation_extractor.base import OriginalTextExtractor
from mapnlp.pipe.base import NLPPipe


class SentenceSplitterPipe(NLPPipe):
    DEFAULT_ANNOTATION_EXTRACTOR = OriginalTextExtractor()
    DEFAULT_ALGORITHM_NAME = "line"
    ALGORITHM_FACTORY_CLASS = SentenceSplitterFactory
