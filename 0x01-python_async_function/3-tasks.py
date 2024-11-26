#!/usr/bin/env python3
"""
module: 3-tasks
description: returns an asyncio task.
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns an asyncio task.
    Args:
        max_delay (int): maximum delay.
    Return:
        task.
    """
    return asyncio.create_task(wait_random(max_delay))
