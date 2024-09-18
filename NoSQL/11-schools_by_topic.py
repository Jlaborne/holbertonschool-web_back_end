#!/usr/bin/env python3
""" Module that returns a list of schools that have a specific topic """


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have a specific topic.
    
    :param mongo_collection: The pymongo collection object
    :param topic: The topic to search for in the schools' topics
    :return: A list of schools that have the specified topic
    """
    return list(mongo_collection.find({"topics": topic}))
