
from typing import List, Dict, Any

from mapnlp.alg.chunking import Chunker
from mapnlp.data.chunk import Chunk
from mapnlp.data.morpheme import Morpheme


@Chunker.registry
class IndependentRuleChunker(Chunker):
    """
    Simple Rule-based Chunker
    where each chunk has only one independent word and some adjunct/other words
    Reference: http://www.nltk.org/book-jp/ch12.html#id56
    """
    ALGORITHM_NAME = "independent-rule"

    def __init__(self):
        pass

    def run(self, morphs: List[Morpheme]) -> List[Chunk]:
        # assert morphs[0].is_independent(), "Head of morpheme should be independent"
        chunks = []
        morph_buff = []
        morph_buff.append(morphs[0])
        for m in morphs[1:]:
            if m.is_independent():  # independent word
                chunks.append(Chunk(morph_buff))
                morph_buff = []
            morph_buff.append(m)
        chunks.append(Chunk(morph_buff))
        return chunks

    @classmethod
    def build(cls, config: Dict[str, Any]):
        return cls()
