#!/usr/bin/env python3
import csv
import math
from typing import List


def index_range(page, page_size):
    '''this function returns the starting and ending positions of
    of the file'''
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


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
        '''apply indes_range to get start and end indices
            and return the correct page
        '''
        assert (isinstance(page, int) and page > 0) and\
            (isinstance(page_size, int) and page_size > 0)
        ret_index = index_range(page, page_size)
        dataset = self.dataset()
        if ret_index[0] > ret_index[1]:
            return []
        elif ret_index[0] > len(dataset):
            return []
        elif ret_index[1] > len(dataset):
            return []
        page = [self.__dataset[data] for data
                in range(ret_index[0], ret_index[1])]
        return page
