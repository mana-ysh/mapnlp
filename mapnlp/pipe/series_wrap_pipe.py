
from typing import Dict, Any, Union

from mapnlp.annotation_extractor.base import AnnotationExtractor
from mapnlp.annotation_extractor.last_text_span_seq_extractor import  LastTextSpanSequenceStringExtractor
from mapnlp.data.base import InputText
from mapnlp.pipe.base import NLPPipe


class SeriesWrapPipe(NLPPipe):
    """
    a series of pipe's process
    usage)
    pipe = SeriesWrapPipe.build_with_wrap("tok-seq", TokenizerPipe, ...)
    """

    DEFAULT_ANNOTATION_EXTRACTOR = LastTextSpanSequenceStringExtractor()

    # TODO: encapsulate series AnnotationExtractor. the argument "ann_extractor" must be series-specific
    def __init__(self, _id: str, alg: Union['Algorithm', 'Annotator'], ann_extractor: AnnotationExtractor):
        super(SeriesWrapPipe, self).__init__(_id, alg, ann_extractor)

    def process(self, input_text: InputText):
        input_list = self._ann_extractor.extract(input_text)
        assert type(input_list) == list, "Input to sequential pipe should be list, not {}".format(type(input_list))
        output_list = [self._alg.run(_input) for _input in input_list]
        self._alg.annotate_series_to_input_text(self._id, input_text, output_list)

    # FIXME: clean args
    @classmethod
    def build_with_wrap(cls, _id: str, inner_pipe_cls: NLPPipe.__class__, alg_config: Dict[str, Any] = None,
                        ann_extractor_config: Dict[str, Any] = None):
        if alg_config is None:
            alg_config = {}
        alg_name = alg_config.get("alg_name", inner_pipe_cls.DEFAULT_ALGORITHM_NAME)
        alg = inner_pipe_cls.ALGORITHM_FACTORY_CLASS.create(alg_name, alg_config.get("params", None))

        assert ann_extractor_config or cls.DEFAULT_ANNOTATION_EXTRACTOR
        if ann_extractor_config is None:
            ann_ext = cls.DEFAULT_ANNOTATION_EXTRACTOR
        else:
            raise NotImplementedError("currently, not available")
        return cls(_id, alg, ann_ext)

    @classmethod
    def build(cls, _id: str, alg_config: Dict[str, Any] = None, ann_extractor_config: Dict[str, Any] = None):
        raise NotImplementedError("please use build_with_wrap")
