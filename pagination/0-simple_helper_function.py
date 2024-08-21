#!/usr/bin/env python3
"""
This module provides a helper function for calculating the range of indices for pagination purposes.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Calculate the start and end indices for a given page and page size.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and end index for the
               items to be displayed on the given page.
    """
    start_index = (page - 1) * page_size
    end_index = page + page_size
    return start_index, end_index
