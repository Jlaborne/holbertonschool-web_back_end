#!/usr/bin/env python3
"""
This module provides a function to create a tuple from a string and
an int/float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an int or float and returns a tuple where the first
    element is the string and the second is the square of the int/float.

    Args:
        k (str): The string key.
        v (Union[int, float]): The value, which can be an int or a float.

    Returns:
        Tuple[str, float]: A tuple with the string and the squared value as
        a float.
    """
    return (k, float(v ** 2))
