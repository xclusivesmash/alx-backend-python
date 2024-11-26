#!/usr/bin/env python3
"""
module: 2-measure_runtime.
description: measures the runtime.
"""
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measures the total execution time.
    Return:
        execution time (s).
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start
