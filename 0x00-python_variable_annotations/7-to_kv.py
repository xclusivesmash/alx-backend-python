#!/usr/bin/env python3
"""
module: 7-to_kv
description: typed annotations.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Type annotations.
    Args:
        k (str): input one.
        v (Union[int, float]): input two.
    Return:
        (tuple): k and square of v.
    """
    return (k, float(v * v))
