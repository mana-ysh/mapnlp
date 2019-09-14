
from typing import List, Dict, Any

from mapnlp.alg.summarization import TextSummarizer
from mapnlp.data.morpheme import Morpheme


@TextSummarizer.registry
class LeadSummarizer(TextSummarizer):
    """
    just pick up head sentences
    """
    ALGORITHM_NAME = "lead"

    def __init__(self, n_head=2):
        self._n_head = n_head

    def run(self, sents: List[List[Morpheme]]) -> str:
        _n_head = min(self._n_head, len(sents))
        ext_sents = ["".join([m.surface for m in s]) for s in sents[:_n_head]]
        return "".join(ext_sents)

    @classmethod
    def build(cls, config: Dict[str, Any]):
        n_head = config.get("n_head", 2)
        return cls(n_head)
