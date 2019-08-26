import json
import uuid
from collections import defaultdict
from typing import List, Tuple, Optional, Dict, Any

from mapnlp.annotation.base import Annotation


class GraphNode():
    def __init__(self,
                 name: str,
                 children: Optional[List['GraphNode']] = None,
                 parent: Optional[List['GraphNode']] = None):
        self.name = name
        self._children = children
        self._parent = parent

    def get_children(self) -> Optional[List['GraphNode']]:
        return self._children

    def get_parent(self) -> Optional[List['GraphNode']]:
        return self._parent

    def set_parent(self, parent):
        self._parent = parent

    def is_leaf(self) -> bool:
        if len(self._children) == 0 or self._children is None:
            return True
        else:
            return False


class SpanTextUnit(GraphNode):
    """
    Span-based text unit (e.g token, chunk, sentence given the original text)
    """
    def __init__(self,
                 surface: str,
                 span: Tuple[int, int],
                 child_units: Optional[List['TreeNode']] = None,
                 parent_units: Optional[List['TreeNode']] = None,
                 info: Optional[Dict[str, Any]] = None
                 ):
        # FIXME: tempolary name
        _name = str(uuid.uuid4())
        super(SpanTextUnit, self).__init__(_name, child_units, parent_units)

        assert span[0] < span[1], "Invalid span: {}".format(span)
        self.surface = surface
        self.start = span[0]
        self.end = span[1]
        self.info = info

    def dumps(self):
        return json.dumps(self.dump_as_dict())

    # as default
    def dump_as_dict(self):
        d = {
            "surface": self.surface,
            "start": self.start,
            "end": self.end
        }

        if (self._children is not None) and (len(self._children) > 0):
            d["children"] = [child.dump_as_dict() for child in self._children]
        return d


class IdentifiedTextUnit(GraphNode):
    """
    Identified text unit (e.g Node of AMR)
    """
    def __init__(self, _id):
        # TODO: implement
        raise NotImplementedError()


class InputText(object):
    def __init__(self, original_text):
        self.original_text = original_text
        self._annotations = {}
        self._alg_name2ann_ids = defaultdict(lambda: [])
        self._last_ann_id = None

    def annotate(self, ann_id: str, alg_name: str, ann: Annotation):
        self._annotations[ann_id] = ann
        self._alg_name2ann_ids[alg_name].append(ann_id)
        self._last_ann_id = ann_id

    def get_last(self) -> Annotation:
        """
        get final analyzed annotation
        """
        if self._last_ann_id is None:
            raise AttributeError("Don't have any annotation now")
        return self._annotations[self._last_ann_id]

    def get_last_alg(self, alg_name: str):
        """
        get last annotation with specific Algorithm name
        """
        ann_id = self._alg_name2ann_ids[alg_name][-1]
        return self._annotations[ann_id]

    def dumps(self):
        # TODO
        d = {"original_text": self.original_text}
        for k in self._annotations.keys():
            d[k] = json.loads(self._annotations[k].dumps())
        return json.dumps(d)