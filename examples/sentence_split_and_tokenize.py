
from mapnlp.pipe.dag import NLPTaskDAG
from mapnlp.pipe.sentence_splitter_pipe import SentenceSplitterPipe
from mapnlp.pipe.series_wrap_pipe import SeriesWrapPipe
from mapnlp.pipe.tokenizer_pipe import TokenizerPipe

import sys
sys.path.append("./")

# NOTE: need to import to register into factory
from alg_impls import line_splitter, sudachi


if __name__ == '__main__':

    sent_splitter = SentenceSplitterPipe.build("sp", {"alg_name": "line"})
    tok_seq = SeriesWrapPipe.build_with_wrap("tok-seq", TokenizerPipe, {"alg_name": "sudachi"})

    dag = NLPTaskDAG("example")

    dag.add_task_dep((NLPTaskDAG.INITIAL, sent_splitter))
    dag.add_task_dep((sent_splitter, tok_seq))

    test_sents = "今日の天気は晴れ.\n明日の天気は曇り"
    res = dag.process(test_sents)
    print(res.dumps())
