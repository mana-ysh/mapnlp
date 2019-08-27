from abc import ABCMeta, abstractmethod
from typing import Union, Any, Dict

from mapnlp.annotator.base import Annotator
from mapnlp.alg.base import Algorithm
from mapnlp.data.base import InputText
from mapnlp.annotation_extractor.base import AnnotationExtractor


class PipeBase(metaclass=ABCMeta):
    @abstractmethod
    def process(self, _input: object):
        raise NotImplementedError()


class NLPPipe(PipeBase):
    DEFAULT_ANNOTATION_EXTRACTOR = None
    DEFAULT_ALGORITHM_NAME = None
    ALGORITHM_FACTORY_CLASS = None

    # NOTE: self is not Union, but Intersection
    def __init__(self, _id: str, alg: Union['Algorithm', 'Annotator'], ann_extractor: AnnotationExtractor):
        if not ann_extractor:
            ann_extractor = self.DEFAULT_ANNOTATION_EXTRACTOR
        self._id = _id
        self._alg = alg
        self._ann_extractor = ann_extractor

    @property
    def id(self):
        return self._id

    def process(self, input_text: InputText):
        _input = self._ann_extractor.extract(input_text)
        output = self._alg.run(_input)
        self._alg.annotate_to_input_text(self._id, input_text, output)

    @classmethod
    def build(cls, _id: str, alg_config: Dict[str, Any] = None, ann_extractor_config: Dict[str, Any] = None):
        if alg_config is None:
            alg_config = {}
        alg_name = alg_config.get("alg_name", cls.DEFAULT_ALGORITHM_NAME)
        alg = cls.ALGORITHM_FACTORY_CLASS.create(alg_name, alg_config.get("params", None))

        assert ann_extractor_config or cls.DEFAULT_ANNOTATION_EXTRACTOR
        if ann_extractor_config is None:
            ann_ext = cls.DEFAULT_ANNOTATION_EXTRACTOR
        else:
            raise NotImplementedError("currently, not available")
        return cls(_id, alg, ann_ext)


class InitialPipe(NLPPipe):
    ID = "INITIAL"

    def __init__(self):
        self._id = self.ID

    def process(self, input_text: InputText):
        # do nothing
        pass