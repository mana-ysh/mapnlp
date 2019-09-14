
from typing import List, Dict, Any

from mapnlp.alg.tokenization.base import Tokenizer
from mapnlp.data.morpheme import Morpheme


@Tokenizer.registry
class CharacterTokenizer(Tokenizer):
    ALGORITHM_NAME = "char"
    POS_TAG = ["", "", "", "", "", ""]

    def __init__(self):
        pass

    def run(self, _input: str) -> List[Morpheme]:
        return [
            Morpheme(char, self.POS_TAG, (i, i+1)) for i, char in enumerate(_input)
        ]

    @classmethod
    def build(cls, config: Dict[str, Any]):
        return cls()
