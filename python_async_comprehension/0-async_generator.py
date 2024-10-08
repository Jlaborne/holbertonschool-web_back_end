#!/usr/bin/env python3
"""Module that contains an asynchronous generator function."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields 10 random numbers between 0 and 10.
    
    The coroutine waits 1 second asynchronously before each yield.
    
    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
