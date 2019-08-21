
from typing import Tuple, Optional, List

from mapnlp.data.base import SpanTextUnit


class Morpheme(SpanTextUnit):
    def __init__(self, surface: str, pos: List[str], span: Tuple[int, int], normalized_form: Optional[str] = None):
        super(Morpheme, self).__init__(surface=surface, span=span)
        self.pos = pos
        self.normalized_form = normalized_form

    @property
    def primary_part_of_speech(self):
        return self.pos[0]

    def is_independent(self) -> bool:
        raise NotImplementedError()


class UnidicMorpheme(Morpheme):
    def __init__(self, surface: str, pos: List[str], span: Tuple[int, int], normalized_form: Optional[str] = None):
        super(UnidicMorpheme, self).__init__(surface=surface, pos=pos, span=span, normalized_form=normalized_form)

    def is_independent(self) -> bool:
        """
            Unidic Grammar
            POS tag list is in General/Sudachi/Dictionary in Notion
        """
        # FIXME: simplify rules and deal with ambiguous POS
        if self.pos[0] == "動詞" and self.pos[1] == "一般":
            return True
        elif self.pos[0] == "名詞" and self.pos[1] != "助動詞語幹":
            return True
        elif self.pos[0] == "形容詞" and self.pos[1] == "一般":
            return True
        elif self.pos[0] == "形状詞" and self.pos[1] != "助動詞語幹":
            return True
        else:
            return False
