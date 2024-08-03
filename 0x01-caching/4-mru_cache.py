#!/usr/bin/env python3
"""
A class MRUCache that inherits
from BaseCaching and is a caching system
"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    A class that replaces cache
    using the most recently used
    algorithm
    """
    def __init__(self):
        """
        Assigns a key to store
        a value 'item'
        """
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """
        Setting the keys
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.usedKeys:
                self.usedKeys.append(key)
            else:
                self.usedKeys.append(
                    self.usedKeys.pop(self.usedKeys.index(key)))
            if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
                discard = self.usedKeys.pop(-2)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """
        Returns the value value in self.cache_data
        linked to key
        """
        if key is not None and key in self.cache_data.keys():
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
            return self.cache_data.get(key)
        return None
