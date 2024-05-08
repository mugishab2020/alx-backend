#!/usr/bin/env python3
'''  Basic dictionary
'''


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    ''' class for basic caching
    '''
    def __init__(self):
        ''' init method
            the constructor
        '''
        super().__init__()

    def put(self, key, item):
        '''add the key and item to self.cache_data
        '''
        if not key or not item:
            return None
        self.cache_data[key] = item

    def get(self, key):
        '''get the item from self.cache_data
        '''
        if not key:
            return None
        return self.cache_data.get(key)
