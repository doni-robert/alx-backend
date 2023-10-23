#!/usr/bin/env python3
""" Contains the `index_range` function """


def index_range(page, page_size):
    """
    Returns a tuple of size teo contining a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters

    Args:
        page(int): the page number
        page_size(int): the page size
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return ((start_index, end_index))
