
from typing import Union, TypeVar

S = TypeVar('S')
T = TypeVar('T')

# NOTE: this is just hinting purpose, NOT union strictly
Intersect = Union[S, T]
