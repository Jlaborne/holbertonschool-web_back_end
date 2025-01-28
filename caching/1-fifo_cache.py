#!/usr/bin/env python3
""" FIFO Cache module """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines a caching system using FIFO algorithm """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []  # To keep track of the insertion order

    def put(self, key, item):
        """ Add an item in the cache using FIFO """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Remove the key from the order if it already exists
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # If the cache exceeds the max limit, remove the first item added
                discarded = self.order.pop(0)
                del self.cache_data[discarded]
                print(f"DISCARD: {discarded}")
            # Add the new key to the cache and to the order list
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
