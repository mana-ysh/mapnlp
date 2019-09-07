
import json
from typing import List, Dict, Any
from warnings import warn

from mapnlp.alg.sentence_splitter.base import SentenceSplitter
from mapnlp.data.sentence import Sentence


@SentenceSplitter.registry
class LineSentenceSplitter(SentenceSplitter):
    ALGORITHM_NAME = "line"

    def __init__(self):
        pass

    def run(self, _input: str) -> List[Sentence]:
        if _input.endswith("\n"):
            warn("Input ends with blank line. Removed")
            _input = _input[:-1]
        lines = _input.split("\n")
        start = 0
        sents = []
        for line in lines:
            sents.append(Sentence(line, (start, start+len(line))))
            start += len(line) + 1
        return sents

    @classmethod
    def build(cls, config: Dict[str, Any]):
        return cls()
