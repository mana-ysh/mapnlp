from abc import ABCMeta, abstractmethod
from collections import defaultdict
from typing import Any, Dict, Optional

from mapnlp.annotation.base import Annotation
from mapnlp.data.base import InputText


class Algorithm(metaclass=ABCMeta):
    TASK_NAME = None
    ALGORITHM_NAME = None
    ALGORITHM_POOL = defaultdict(dict)
    @abstractmethod
    def run(self, _input: Any) -> Any:
        raise NotImplementedError()

    @classmethod
    def annotate_from_output(cls, input_text: InputText, alg_output) -> Annotation:
        raise ValueError("Please setup annotation method via annotation helper for your algorithm")

    @classmethod
    def build(cls, config: Dict[str, Any]):
        raise NotImplementedError()

    @classmethod
    def registry(cls, impl_cls):
        """
        register to Algorithm pool for factory
        :param impl_cls: subclass of Algorithm
        """
        cls.ALGORITHM_POOL[cls.TASK_NAME][impl_cls.ALGORITHM_NAME] = impl_cls

    @classmethod
    def get_task_algorithms(cls):
        return cls.ALGORITHM_POOL[cls.TASK_NAME]


class AlgorithmFactory():
    NAME2CLASS = {}

    @classmethod
    def create(cls, name: str, config: Optional[Dict[str, Any]] = None) -> Algorithm:
        if len(cls.NAME2CLASS) == 0:
            raise RuntimeError("Please register your algorithm")

        alg_class = cls.NAME2CLASS.get(name, None)
        if alg_class is None:
            raise ValueError("Invalid algorithm name: {}\nPlease select from here: {}"
                             .format(name, list(cls.NAME2CLASS.keys())))
        if config is None:
            config = {}
        return alg_class.build(config)