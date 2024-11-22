#!/usr/bin/env python3
"""
module: 6-sum_mixed_list
description: mixed types.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Type annotations.
    Args:
        mxd_lst (List[Union[int, float]]): mized list.
    Return:
        (float): sum.
    """
    return float(sum(mxd_lst))
