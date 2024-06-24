#!/usr/bin/env python3
""" Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    returns a tuple of size with start
     index and end index corresponding to 
     range of indexes to return in list for
     those particular pagination parameters
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
