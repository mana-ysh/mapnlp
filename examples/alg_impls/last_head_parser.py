
from typing import List, Dict, Any

from mapnlp.alg.dep_parser import DependencyParser
from mapnlp.data.dep_edge import DependencyEdge
from mapnlp.data.base import SpanTextUnit


@DependencyParser.registry
class LastHeadDependencyParser(DependencyParser):
    """
    All units except the last one are modifier
    """
    ALGORITHM_NAME = "last-head"

    def __init__(self):
        pass

    def run(self, units: List[SpanTextUnit]) -> List[DependencyEdge]:
        num = len(units)
        # children
        labels = [DependencyEdge(num-1, i) for i in range(num - 1)]
        return labels

    @classmethod
    def build(cls, config: Dict[str, Any]):
        return cls()
