
import json
from typing import List, Dict, Any

from sudachipy import tokenizer, dictionary, config
from sudachipy.morpheme import Morpheme as SudachiMorphme

from mapnlp.alg.tokenization.base import Tokenizer
from mapnlp.data.morpheme import UnidicMorpheme


@Tokenizer.registry
class SudachiTokenizer(Tokenizer):
    ALGORITHM_NAME = "sudachi"

    def __init__(self, mode='C', dic_name=None):  # FIXME: mode as string obj
        """
        args:
            - mode (str): split mode
            - dic_name (str): dictionary file name. This dict must be located in SudachiPy/resouces (core, full or user dict)
        """
        if mode == 'A':
            self.mode = tokenizer.Tokenizer.SplitMode.A
        elif mode == 'B':
            self.mode = tokenizer.Tokenizer.SplitMode.B
        elif mode == 'C':
            self.mode = tokenizer.Tokenizer.SplitMode.C
        else:
            raise ValueError("Invalid mode: {}".format(mode))

        with open(config.SETTINGFILE, "r", encoding="utf-8") as f:
            settings = json.load(f)
        if dic_name != None:
            settings["systemDict"] = dic_name
        self._tokenizer_obj = dictionary.Dictionary(settings).create()

    def run(self, _input: str) -> List[UnidicMorpheme]:
        return [convert_sudachi_morpheme(m)
                for m in self._tokenizer_obj.tokenize(self.mode, _input)]

    @classmethod
    def build(cls, config: Dict[str, Any]):
        mode = config.get("mode", "C")
        dic_name = config.get("dic_name", None)
        return cls(mode, dic_name)


def convert_sudachi_morpheme(sudachi_morph: SudachiMorphme) -> UnidicMorpheme:
    return UnidicMorpheme(
        sudachi_morph.surface(),
        sudachi_morph.part_of_speech(),
        (sudachi_morph.begin(), sudachi_morph.end()),
        sudachi_morph.normalized_form()
    )
