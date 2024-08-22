#!/usr/bin/env python3
"""Module that updates the topics of a school document based on the school name"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the school name.
    
    :param mongo_collection: The pymongo collection object
    :param name: The name of the school to update
    :param topics: A list of topics to set for the school
    """
    mongo_collection.update.many(
        {"name": name},          # Filter by the school name
        {"$set": {"topics": topics}}  # Set the topics field to the new list
    )
