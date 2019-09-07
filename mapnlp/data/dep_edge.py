
import json


class DependencyEdge():
    def __init__(self, head_idx, modifier_idx, label=None):
        self.head_idx = head_idx
        self.modifier_idx = modifier_idx
        self.label = label

    # FIXME: unify
    def dump_as_dict(self):
        return {
            "head_index": self.head_idx,
            "modifier_index": self.modifier_idx,
            "label": self.label
        }

    def dumps(self):
        return json.dumps(self.dump_as_dict())
