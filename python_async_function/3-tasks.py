#!/usr/bin/env python3
"""
Task 3
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task.

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: A task object wrapping the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
