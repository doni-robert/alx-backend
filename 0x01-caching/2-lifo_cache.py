#!/usr/bin/env python3
""" LIFOCache module """
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache    caching system
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
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    k, v = self.cache_data.popitem()
                    print(f'DISCARD: {k}')
                else:
                    self.cache_data.pop(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item by key
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
