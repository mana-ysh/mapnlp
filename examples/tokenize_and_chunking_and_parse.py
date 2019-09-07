
from mapnlp.pipe.dag import NLPTaskDAG
from mapnlp.pipe.chunker_pipe import ChunkerPipe
from mapnlp.pipe.dependency_parser_pipe import DependencyParserPipe
from mapnlp.pipe.tokenizer_pipe import TokenizerPipe

import sys
sys.path.append("./")

# NOTE: need to import to register into factory
from alg_impls import sudachi, rule_chunker, last_head_parser


if __name__ == '__main__':

    tok = TokenizerPipe.build("tok", {"alg_name": "sudachi"})
    chunk = ChunkerPipe.build("chunk", {"alg_name": "independent-rule"})
    parse = DependencyParserPipe.build("dep", {"alg_name": "last-head"})

    dag = NLPTaskDAG("example")

    dag.add_task_dep((NLPTaskDAG.INITIAL, tok))
    dag.add_task_dep((tok, chunk))
    dag.add_task_dep((chunk, parse))

    res = dag.process("すもももももももものうち")
    print(res.dumps())
