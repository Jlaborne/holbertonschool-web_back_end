#!/usr/bin/env python3
"""Basic Redis cache with method call counting"""

import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional


def call_history(method: Callable) -> Callable:
    """Decorator to store history of inputs and outputs in Redis lists."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key_input = method.__qualname__ + ':inputs'
        key_output = method.__qualname__ + ':outputs'

        self._redis.rpush(key_input, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(key_output, result)

        return result

    return wrapper


def count_calls(method: Callable) -> Callable:
    """Decorator to count how many times a method is called."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def replay(method: Callable) -> Callable:
    """Display the history of calls of a function."""
    r = redis.Redis()
    method_name = method.__qualname__
    inputs_key = f"{method_name}:inputs"
    outputs_key = f"{method_name}:outputs"

    inputs = r.lrange(inputs_key, 0, -1)
    outputs = r.lrange(outputs_key, 0, -1)

    print(f"{method_name} was called {len(inputs)} times:")

    for input_data, output_data in zip(inputs, outputs):
        args_str = input_data.decode("utf-8")
        result_str = output_data.decode("utf-8")
        print(f"{method_name}(*{args_str}) -> {result_str}")


class Cache:
    def __init__(self):
        """Initialize Redis client and flush existing data"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the data in Redis using a random UUID key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[bytes, str, int, None]:
        """Get data from Redis and optionally apply a conversion function"""
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve value as UTF-8 string"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve value as integer"""
        return self.get(key, fn=int)
