#!/usr/bin/env python3
'''this function returns the starting and ending positions of
of the file'''


def index_range(page, page_size):
    '''this function returns the starting and ending positions of
    of the file'''
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
