#!/usr/bin/env python3
"""
A Python function that returns a tuple
of size two containing a start index
and an end index corresponding to the
range of indexes to return in a list
for those particular pagination parameters.
"""


# Import statements
import csv
import math
from typing import Tuple  # For Type annotations
from typing import List  # For Type Annotations


def index_range(page: int, page_size: int) -> Tuple:
    """
    Returns a table for
    a size of pagination
    """
    start_page = (page - 1) * page_size
    page_size = page * page_size
    myTuple = (start_page, page_size)
    return myTuple


# Add code from intranet
class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the right dataset and
        correctly paginates it
        """
        # Asserting if page and page_size are
        # integers and are greater than zero
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        #
        # Using the index_range function
        # to find the correct indexes
        # and paginate the dataset correctly
        dataset = self.dataset()
        #
        try:
            # Loading from the dataset
            start_index, final_index = index_range(page, page_size)
            fetchedData = dataset[start_index:final_index]
            return fetchedData
        except IndexError:  # If out of range
            # Return an empty list if out of range
            return []
        # pass
