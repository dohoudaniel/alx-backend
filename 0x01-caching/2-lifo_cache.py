#!/usr/bin/env python3
"""
A class LIFOCache that inherits
from BaseCaching and is a caching system
"""


# Import statements
from base_caching import BaseCaching

# Maximum items from the BaseCaching class
# maxItems = BaseCaching.MAX_ITEMS


class FIFOCache(BaseCaching):
    """
    Acts as a Cache but
    using the FIFO method
    """

    def __init__(self):
        """
        The initialization method
        importing from the
        BaseCaching method
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns a key to store
        a value 'item'
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                listOfCacheKeys = list(iter(self.cache_data.keys()))
                lastKey = listOfCacheKeys[-1]
                del self.cache_data[lastKey]
                print(f"DISCARD: {lastKey}")

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
