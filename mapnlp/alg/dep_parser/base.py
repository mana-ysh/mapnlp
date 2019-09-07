
from typing import List

from mapnlp.annotator.sequential import DependencyLabelSequentialAnnotator
from mapnlp.alg.base import Algorithm, AlgorithmFactory
from mapnlp.data.base import SpanTextUnit
from mapnlp.data.dep_edge import DependencyEdge


class DependencyParser(Algorithm, DependencyLabelSequentialAnnotator):
    TASK_NAME = "dependency-parser"

    def run(self, _input: List[SpanTextUnit]) -> List[DependencyEdge]:
        raise NotImplementedError()


class DependencyParserFactory(AlgorithmFactory):
    NAME2CLASS = DependencyParser.ALGORITHM_POOL[DependencyParser.TASK_NAME]
