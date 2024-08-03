#!/usr/bin/env python3
"""
A class LRUCache that inherits
from BaseCaching and is a caching system
"""


# Import statements
from base_caching import BaseCaching

# Maximum items from the BaseCaching class
# maxItems = BaseCaching.MAX_ITEMS


class LRUCache(BaseCaching):
    """
    Acts as a Cache but
    using the FIFO method
    """

    def __init__(self):
        """
        A class that replaces cache
        using the most recently used
        algorithm
        """
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """
        Assigns a key to store
        a value 'item'
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.usedKeys:
                self.usedKeys.append(key)
            else:
                self.usedKeys.append(
                    self.usedKeys.pop(self.usedKeys.index(key)))
            if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
                discard = self.usedKeys.pop(0)
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
