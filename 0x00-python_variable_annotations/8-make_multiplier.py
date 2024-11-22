#!/usr/bin/env python3
"""
module: 8-make_multiplier
description: type annotations
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates a multiplier function.
    """
    return lambda x: x * multiplier
