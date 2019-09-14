
from typing import List, Dict, Any

from mapnlp.alg.chunking import Chunker
from mapnlp.data.chunk import Chunk
from mapnlp.data.morpheme import Morpheme


@Chunker.registry
class NgramChunker(Chunker):
    ALGORITHM_NAME = "ngram"

    def __init__(self, n):
        self.n = n

    def run(self, morphs: List[Morpheme]) -> List[Chunk]:
        # assert morphs[0].is_independent(), "Head of morpheme should be independent"
        chunks = []
        indices = list(range(0, len(morphs), self.n))
        for i in range(len(indices) - 1):
            chunks.append(Chunk(morphs[indices[i]: indices[i+1]]))
        chunks.append(Chunk(morphs[indices[-1]:]))
        return chunks

    @classmethod
    def build(cls, config: Dict[str, Any]):
        n = config.get("n", 2)
        return cls(n)
