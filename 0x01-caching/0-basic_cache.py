#!/usr/bin/env python3
""" BasicCache module """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache caching system
    """
    def __init__(self):
        """ Initialize """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item by key
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
