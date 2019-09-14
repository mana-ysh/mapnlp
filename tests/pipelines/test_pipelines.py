
import json
from typing import List, Dict, Any
from unittest import TestCase

# TODO: remove dependency
from sudachipy import tokenizer, dictionary, config
from sudachipy.morpheme import Morpheme as SudachiMorphme

from mapnlp.alg.chunking import Chunker
from mapnlp.alg.tokenization import Tokenizer
from mapnlp.data.chunk import Chunk
from mapnlp.data.morpheme import Morpheme, UnidicMorpheme
from mapnlp.pipe.dag import NLPTaskDAG
from mapnlp.pipe.chunker_pipe import ChunkerPipe
from mapnlp.pipe.tokenizer_pipe import TokenizerPipe


class TestPipelines(TestCase):

    def test_tokenize_and_chunking(self):
        tok = TokenizerPipe.build("tok", {"alg_name": "sudachi"})
        chunk = ChunkerPipe.build("chunk", {"alg_name": "independent-rule"})

        dag = NLPTaskDAG("example")
        dag.add_task_dep((NLPTaskDAG.INITIAL, tok))
        dag.add_task_dep((tok, chunk))

        # FIXME: write test case
        res = dag.process("すもももももももものうち")


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
