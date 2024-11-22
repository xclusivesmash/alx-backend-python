#!/usr/bin/env python3
"""
module: 5-sum_list
description: sums list items.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Type annotations.
    Args:
        input_list (list[float]): list of float items.
    Return:
        (float): sum.
    """
    return float(sum(input_list))
