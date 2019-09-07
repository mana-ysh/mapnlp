
from mapnlp.alg.dep_parser import DependencyParserFactory
from mapnlp.annotation_extractor.last_text_span_seq_extractor import LastTextSpanSequenceStringExtractor
from mapnlp.pipe.base import NLPPipe


class DependencyParserPipe(NLPPipe):
    DEFAULT_ANNOTATION_EXTRACTOR = LastTextSpanSequenceStringExtractor()
    DEFAULT_ALGORITHM_NAME = "last-head"
    ALGORITHM_FACTORY_CLASS = DependencyParserFactory
