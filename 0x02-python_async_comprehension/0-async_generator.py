#!/usr/bin/env python3
"""
module: 0-async_generator
description: yields a random number [0, 10]
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """yield integers.
    Return:
        list of number btw. 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
