#!/usr/bin/env python3
""" List all documents in a collection """


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.
    
    :param mongo_collection: The pymongo collection object
    :return: A list of all documents in the collection, or an empty list if no documents are found
    """
    return list(mongo_collection.find())
