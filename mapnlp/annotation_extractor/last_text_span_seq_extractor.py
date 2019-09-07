
from typing import List, Optional

from mapnlp.data.base import InputText
from mapnlp.annotation_extractor.base import AnnotationExtractor


class LastTextSpanSequenceStringExtractor(AnnotationExtractor):
    def __init__(self):
        pass

    def extract(self, input_text: InputText) -> List[str]:
        morphs_ann = input_text.get_last()
        text_spans = morphs_ann.get("sequential")
        return [s.surface for s in text_spans]
