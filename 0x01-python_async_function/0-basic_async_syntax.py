#!/usr/bin/env python3
"""
module: basic_async_syntax
description: syntax based exec.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This function waits for a random delay between 0 and max_delay.
    Args:
        max_delay (int): maximum delay to wait.
    Returns:
        None
    """
    seconds: float = random.random() * max_delay
    await asyncio.sleep(seconds)
    return seconds
