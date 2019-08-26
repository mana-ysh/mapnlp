
from typing import List

from mapnlp.data.base import SpanTextUnit
from mapnlp.data.morpheme import Morpheme


class Chunk(SpanTextUnit):
    def __init__(self, morphs: List['Morpheme']):
        surface = "".join([m.surface for m in morphs])
        span = (morphs[0].start, morphs[-1].end)
        super(Chunk, self).__init__(surface=surface, span=span, child_units=morphs)