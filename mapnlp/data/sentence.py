
from typing import List, Tuple, Optional

from mapnlp.data.base import SpanTextUnit


class Sentence(SpanTextUnit):
    def __init__(self,
                 surface: str,
                 span: Tuple[int, int],
                 child_units: Optional[List['SpanTextUnit']] = None,
                 parent_units: Optional[List['SpanTextUnit']] = None):
        super(Sentence, self).__init__(surface=surface, span=span, child_units=child_units, parent_units=parent_units)

