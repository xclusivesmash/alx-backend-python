#!/usr/bin/env python3
"""
module: 4-tasks
description: seond version of wait_n
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes task_wait_random n times.
    Args:
        n (int): counter.
        max_delay (int): maximum delay.
    Return:
        list of times.
    """
    times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(times)
