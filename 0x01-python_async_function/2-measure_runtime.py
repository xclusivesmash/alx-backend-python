#!/usr/bin/env python3
"""
module: 2-meaasure_runtime
description: measures the execution time.
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures execution time
    Args:
        n (int): counter.
        max_delay (int): maximum delay.
    Return:
        execution time.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    t: float = (end - start) / n
    return t
