
from mapnlp.alg.tokenization import TokenizerFactory
from mapnlp.annotation_extractor.base import OriginalTextExtractor
from mapnlp.pipe.base import NLPPipe


class TokenizerPipe(NLPPipe):
    DEFAULT_ANNOTATION_EXTRACTOR = OriginalTextExtractor()
    DEFAULT_ALGORITHM_NAME = "sudachi"  # TODO: remove or implement default alg
    ALGORITHM_FACTORY_CLASS = TokenizerFactory
