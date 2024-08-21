#!/usr/bin/env python3
"""
Hypermedia pagination module.
"""
import csv
import math
from typing import List, Dict, Any, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for a given page and page size.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index
                         for the items to be displayed on the given page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a dataset of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server with the dataset."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache the dataset if it hasn't been loaded yet.

        Returns:
            List[List]: The loaded dataset, where each row is a list of values.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of data from the dataset.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows representing the page of data.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Return a dictionary containing pagination metadata and the data.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            Dict[str, Any]: A dictionary containing the pagination details
                            and the data for the current page.
        """
        # Ensure page_size is not zero
        if page_size <= 0:
            raise ValueError("page_size must be greater than 0")

        # Get the data for the current page
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())

        # Calculate the total number of pages
        if page_size > 0:
            total_pages = math.ceil(total_items / page_size)
        else:
            total_pages = 0

        # Determine next and previous pages
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
