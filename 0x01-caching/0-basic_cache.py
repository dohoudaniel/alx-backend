#!/usr/bin/env python3
"""
A class BasicCache that inherits
from BaseCaching and is a caching system
"""


# Import statements
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Inherits from BaseCaching and
    acts as a caching system.

    Use the self.cache_data from the parent class
    This caching system does not have a limit
    It has two methods:
        - put(self, key, item): Assigns to a dict
        - get(self, key): Returns the value linked to a key
    """
    def __init__(self):
        """
        The initialization method
        that inherits from the
        init method of the parent class
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns to the dictionary self.cache_data
        the 'item' value for the key 'key'
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value value in self.cache_data
        linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        value = self.cache_data.get(key)
        return value
