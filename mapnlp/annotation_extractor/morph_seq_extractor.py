
from typing import List, Optional

from mapnlp.data.base import InputText
from mapnlp.data.morpheme import Morpheme
from mapnlp.annotation_extractor.base import AnnotationExtractor


class MorphSequenceExtractor(AnnotationExtractor):
    def __init__(self, filtered_pos_list: Optional[List[str]] = None):
        if filtered_pos_list is None:
            filtered_pos_list = []
        self._filtered_pos_list = filtered_pos_list

    def extract(self, input_text: InputText) -> List[Morpheme]:
        morphs_ann = input_text.get_last_alg("tokenizer")
        morphs = morphs_ann.get("sequential")
        return [m for m in morphs if m.primary_part_of_speech not in self._filtered_pos_list]


class MorphSequenceStringExtractor(AnnotationExtractor):
    def __init__(self, use_normalized_form: bool = False, filtered_pos_list: Optional[List[str]] = None):
        if filtered_pos_list is None:
            filtered_pos_list = []
        self._use_normalized_form = use_normalized_form
        self._filtered_pos_list = filtered_pos_list

    def extract(self, input_text: InputText) -> List[str]:
        morphs_ann = input_text.get_last_alg("tokenizer")
        morphs = morphs_ann.get("sequential")
        if self._use_normalized_form:
            return [m.normalized_form for m in morphs if m.primary_part_of_speech not in self._filtered_pos_list]
        else:
            return [m.surface for m in morphs if m.primary_part_of_speech not in self._filtered_pos_list]


class MorphSequenceSeriesExtractor(AnnotationExtractor):
    def __init__(self, filtered_pos_list: Optional[List[str]] = None):
        if filtered_pos_list is None:
            filtered_pos_list = []
        self._filtered_pos_list = filtered_pos_list

    def extract(self, input_text: InputText) -> List[List[Morpheme]]:
        morphs_series_ann = input_text.get_last_alg("tokenizer")
        seqs = morphs_series_ann.get("series")
        return [
            [m for m in seq.get("sequential") if m.primary_part_of_speech not in self._filtered_pos_list]
            for seq in seqs
        ]
