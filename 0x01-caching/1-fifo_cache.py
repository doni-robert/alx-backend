#!/usr/bin/env python3
""" FifoCache module """
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FifoCache caching system
    """
    def __init__(self):
        """ Initialize """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key and item:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
                    key not in self.cache_data):
                k, v = self.cache_data.popitem(last=False)
                print(f'DISCARD: {k}')
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item by key
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
