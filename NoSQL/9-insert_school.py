#!/usr/bin/env python3
"""Module  inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection based on kwargs.
    
    :param mongo_collection: The pymongo collection object
    :param kwargs: Keyword arguments representing the document fields and values
    :return: The _id of the newly created document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
