#!/usr/bin/env python
"""
module: basic_async_syntax
description: syntax based exec.
"""
import asyncio


async def wait_random(max_delay: int = 10):
    """
    This function waits for a random delay between 0 and max_delay.
    Args:
        max_delay (int): maximum delay to wait.
    Returns:
        None
    """