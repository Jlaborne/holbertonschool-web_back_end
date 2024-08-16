#!/usr/bin/env python3
"""
This module provides a function that returns a function to multiply a float
by a given multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the multiplied value.
    """
    def multiply_by(value: float) -> float:
        return value * multiplier

    return multiply_by
