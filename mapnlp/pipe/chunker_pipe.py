
from mapnlp.alg.chunking import ChunkerFactory
from mapnlp.annotation_extractor.morph_seq_extractor import MorphSequenceExtractor
from mapnlp.pipe.base import NLPPipe


class ChunkerPipe(NLPPipe):
    DEFAULT_ANNOTATION_EXTRACTOR = MorphSequenceExtractor()
    DEFAULT_ALGORITHM_NAME = "independent-rule"
    ALGORITHM_FACTORY_CLASS = ChunkerFactory
