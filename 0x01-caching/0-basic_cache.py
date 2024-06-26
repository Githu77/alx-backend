#!/usr/bin/env python3
""" A Basic ditionary """


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Cache class inheriting from BaseCaching
    """

    def put(self, key, item):
        """
        assign to dictionary self.cache_data
        item value for the key key.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        returns the value in self.cache_data linked to key.
        """
        return self.cache_data.get(key, None)
