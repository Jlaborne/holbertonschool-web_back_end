#!/usr/bin/env python3
""" MRU Cache module """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines a caching system using MRU algorithm """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []  # To track the usage order of keys (MRU)

    def put(self, key, item):
        """ Add an item in the cache using MRU """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Key exists, update its position
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # If the cache exceeds max limit,
                # remove the most recently used item
                mru_key = self.order.pop(-1)
                # Last key in the order is the most recently used
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")
            # Add the new key to the cache and update usage order
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key and update its usage """
        if key is not None and key in self.cache_data:
            # Update the usage order since the key was accessed
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
