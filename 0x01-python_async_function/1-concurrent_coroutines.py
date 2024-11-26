#!/usr/bin/env python3
"""
module: 1-concurrent_coroutines
description: using wait_random function
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawns wait_random n times.
    Args:
        n (int): counter.
        max_delay (int): maximum delay.
    Return:
        list of delays.
    """
    times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(times)
