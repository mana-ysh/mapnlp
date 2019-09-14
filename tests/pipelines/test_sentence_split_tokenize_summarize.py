from unittest import TestCase

from mapnlp.pipe.dag import NLPTaskDAG
from mapnlp.pipe.chunker_pipe import ChunkerPipe
from mapnlp.pipe.sentence_splitter_pipe import SentenceSplitterPipe
from mapnlp.pipe.series_wrap_pipe import SeriesWrapPipe
from mapnlp.pipe.summarization_pipe import TextSummarizerPipe
from mapnlp.pipe.tokenizer_pipe import TokenizerPipe


class TestSentenceSplitTokenizeSummarize(TestCase):
    SENTENCE_SPLITTER_CONFIG = {
        "id": "sp",
        "alg_config": {
            "alg_name": "line",
            "params": {}
        }
    }

    SERIES_TOKENIZER_CONFIG = {
        "id": "tok-series",
        "pipe_cls": TokenizerPipe,
        "alg_config": {
            "alg_name": "char",
            "params": {}
        }
    }

    SUMMARIZER_CONFIG = {
        "id": "summ",
        "alg_config": {
            "alg_name": "lead",
            "params": {
                "n_head": 2
            }
        }
    }

    @classmethod
    def setUpClass(cls) -> None:
        sp = SentenceSplitterPipe.build(cls.SENTENCE_SPLITTER_CONFIG["id"], cls.SENTENCE_SPLITTER_CONFIG["alg_config"])
        tok_seq = SeriesWrapPipe.build_with_wrap(
            cls.SERIES_TOKENIZER_CONFIG["id"],
            cls.SERIES_TOKENIZER_CONFIG["pipe_cls"],
            cls.SERIES_TOKENIZER_CONFIG["alg_config"]
        )
        summ = TextSummarizerPipe.build(cls.SUMMARIZER_CONFIG["id"], cls.SUMMARIZER_CONFIG["alg_config"])
        cls.dag = NLPTaskDAG("example")
        cls.dag.add_task_dep((NLPTaskDAG.INITIAL, sp))
        cls.dag.add_task_dep((sp, tok_seq))
        cls.dag.add_task_dep((tok_seq, summ))

    def test_tokenize_chunk_parse(self):
        result = self.dag.process("abcde\nfghij\nklm")
        result_dump_dict = result.dump_as_dict()
        self.assertIn("sp", result_dump_dict)
        self.assertIn("tok-series", result_dump_dict)
        self.assertIn("summ", result_dump_dict)

        sp_result = result_dump_dict["sp"]
        self.assertIn("sequential", sp_result)

        tok_series_result = result_dump_dict["tok-series"]
        self.assertIn("series", tok_series_result)
        self.assertTrue(all(["sequential" in each for each in tok_series_result["series"]]))

        summ_result = result_dump_dict["summ"]
        self.assertIn("text", summ_result)

    @classmethod
    def tearDownClass(cls) -> None:
        pass
