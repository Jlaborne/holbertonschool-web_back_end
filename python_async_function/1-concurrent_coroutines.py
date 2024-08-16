#!/usr/bin/env python3
"""
Task 1
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay
    and return the list of all the delays in ascending order.
    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay for each wait_random call.
    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
