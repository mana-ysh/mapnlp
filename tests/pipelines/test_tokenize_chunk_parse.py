
from unittest import TestCase

from mapnlp.pipe.dag import NLPTaskDAG
from mapnlp.pipe.chunker_pipe import ChunkerPipe
from mapnlp.pipe.dependency_parser_pipe import DependencyParserPipe
from mapnlp.pipe.tokenizer_pipe import TokenizerPipe


class TestTokenizeChunkParse(TestCase):
    TOKENIZER_CONFIG = {
        "id": "tok",
        "alg_config": {
            "alg_name": "char",
            "params": {}
        }
    }

    CHUNKER_CONFIG = {
        "id": "chunk",
        "alg_config": {
            "alg_name": "ngram",
            "params": {
                "n": 3
            }
        }
    }

    PARSER_CONFIG = {
        "id": "parser",
        "alg_config": {
            "alg_name": "last-head",
            "params": {}
        }
    }

    @classmethod
    def setUpClass(cls) -> None:
        tok = TokenizerPipe.build(cls.TOKENIZER_CONFIG["id"], cls.TOKENIZER_CONFIG["alg_config"])
        chunk = ChunkerPipe.build(cls.CHUNKER_CONFIG["id"], cls.CHUNKER_CONFIG["alg_config"])
        dep = DependencyParserPipe.build(cls.PARSER_CONFIG["id"], cls.PARSER_CONFIG["alg_config"])
        cls.dag = NLPTaskDAG("example")
        cls.dag.add_task_dep((NLPTaskDAG.INITIAL, tok))
        cls.dag.add_task_dep((tok, chunk))
        cls.dag.add_task_dep((chunk, dep))

    def test_tokenize_chunk_parse(self):
        result = self.dag.process("abcde")
        result_dump_dict = result.dump_as_dict()
        self.assertIn("tok", result_dump_dict)
        self.assertIn("chunk", result_dump_dict)
        self.assertIn("parser", result_dump_dict)

        tok_result = result_dump_dict["tok"]
        self.assertIn("sequential", tok_result)

        chunk_result = result_dump_dict["chunk"]
        self.assertIn("sequential", chunk_result)

        parser_result = result_dump_dict["parser"]
        self.assertIn("sequential", parser_result)

    @classmethod
    def tearDownClass(cls) -> None:
        pass

