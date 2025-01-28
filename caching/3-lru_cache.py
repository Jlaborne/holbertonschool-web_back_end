#!/usr/bin/env python3
""" LRU Cache module """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines a caching system using LRU algorithm """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []  # To track the usage order of keys (LRU)

    def put(self, key, item):
        """ Add an item in the cache using LRU """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Key exists, update its usage
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # If the cache exceeds the max limit,
                # remove the least recently used item
                lru_key = self.order.pop(0)  
                # First key in order is the least recently used
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")
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
