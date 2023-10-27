#!/usr/bin/env python3
""" MRUCache module """
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


MRU_list = []


class MRUCache(BaseCaching):
    """
    MRUCache    caching system
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
            MRU_list.append(key)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    self.cache_data.pop(MRU_list[-2])
                    print(f'DISCARD: {MRU_list[-2]}')
                    MRU_list.pop(-2)
                else:
                    self.cache_data.pop(key)
                    MRU_list.remove(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item by key
        """
        if key and key in self.cache_data:
            MRU_list.remove(key)
            MRU_list.append(key)
            return self.cache_data[key]
        else:
            return None
