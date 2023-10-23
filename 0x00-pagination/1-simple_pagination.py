#!/usr/bin/env python3
""" Contains the class Server"""
import csv
import math
from typing import List


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
        Gets the page indexes
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
   
        result = index_range(page, page_size)
        data = self.dataset()
        if result:
            return data[result[0]:result[1]]
        else:
            return []


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
