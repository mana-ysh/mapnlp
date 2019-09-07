from typing import Any, Union, List

from mapnlp.alg.base import Algorithm
from mapnlp.annotation.base import Annotation, SeriesAnnotation
from mapnlp.data.base import InputText


class Annotator(object):
    """
    attach annotation function into Algorithm class.
    basically this class is jointly inherited Algorithm class.
    """
    @staticmethod
    def _convert_alg_output(alg_output: Any) -> Annotation:
        raise NotImplementedError()

    # NOTE: self is not Union, but Intersection
    def annotate_to_input_text(self: Union['Algorithm', 'Annotator'], ann_id: str, input_text: InputText, alg_output: Any):
        ann = self._convert_alg_output(alg_output)
        input_text.annotate(ann_id, self.TASK_NAME, ann)

    # for annotating via series wrap pipe
    def annotate_series_to_input_text(self: Union['Algorithm', 'Annotator'], ann_id: str,
                                      input_text: InputText, alg_outputs: List[Any]):
        ann_list = [self._convert_alg_output(out) for out in alg_outputs]
        ann = SeriesAnnotation(ann_list)
        input_text.annotate(ann_id, self.TASK_NAME, ann)


# TODO: currently unnecessary
def annotation_by(alg_cls: Algorithm, ann_cls: Annotator):
    def add_annotate_func(*args, **kwargs):
        # TODO: implement to add annotate method into Algorithm
        pass
    return add_annotate_func
