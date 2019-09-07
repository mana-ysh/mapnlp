
import json
from typing import Generic, TypeVar, Optional, Dict, Any, Iterable, List


T = TypeVar('T')


class Annotation(object):
    def __init__(self, content: Dict[str, Any]):
        self.content = content

    def get(self, key: str, default: Any = None):
        if default is None:
            return self.content[key]
        else:
            return self.content.get(key, default)

    def dumps(self):
        # as default
        return json.dumps(self.content)


class SequentialAnnotation(Annotation, Generic[T]):
    def __init__(self, content_list: Iterable[T]):
        content = {"sequential": content_list}
        super(SequentialAnnotation, self).__init__(content)

    def dumps(self):
        key = "sequential"
        d = {key: [json.loads(inner_content.dumps()) for inner_content in self.get(key)]}
        return json.dumps(d)


class SeriesAnnotation(Annotation):
    def __init__(self, ann_list: List[Annotation]):
        content = {"series": ann_list}
        super(SeriesAnnotation, self).__init__(content)

    def dumps(self):
        key = "series"
        d = {key: [json.loads(inner_content.dumps()) for inner_content in self.get(key)]}
        return json.dumps(d)


class LabelAnnotation(Annotation):
    def __init__(self, label: int, name: Optional[str] = None):
        content = {"label": label, "name": name}
        super(LabelAnnotation, self).__init__(content)


def build() -> SequentialAnnotation[int]:
    return SequentialAnnotation()