#!/usr/bin/env python3
"""
A Python function that returns a tuple
of size two containing a start index
and an end index corresponding to the
range of indexes to return in a list
for those particular pagination parameters.
"""


# Import statements
from typing import Tuple  # For Type annotations


def index_range(page: int, page_size: int) -> Tuple:
    """
    Returns a table for
    a size of pagination
    """
    start_page = (page - 1) * page_size
    page_size = page * page_size
    myTuple = (start_page, page_size)
    return myTuple
