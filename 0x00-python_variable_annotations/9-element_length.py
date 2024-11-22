#!/usr/bin/env python3
"""
module: 9-element_length
description: type annotations.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Computes the length of a list of sequences.
    Args:
        lst (Iterable[Sequence]): input one.
    Return:
        (List[Tuple[Sequence, int]]): output.
    """
    return [(i, len(i)) for i in lst]
