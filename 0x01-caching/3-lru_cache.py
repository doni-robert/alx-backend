#!/usr/bin/env python3
""" LRUCache module """
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


LRU_list = []


class LRUCache(BaseCaching):
    """
    LRUCache    caching system
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
            LRU_list.append(key)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    self.cache_data.pop(LRU_list[0])
                    print(f'DISCARD: {LRU_list[0]}')
                    LRU_list.pop(0)
                else:
                    self.cache_data.pop(key)
                    LRU_list.remove(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item by key
        """
        if key and key in self.cache_data:
            LRU_list.remove(key)
            LRU_list.append(key)
            return self.cache_data[key]
        else:
            return None
