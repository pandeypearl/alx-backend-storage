#!/usr/bin/env python3
""" Defines Schools_by_topic """


def schools_by_topic(mongo_collection, topic):
    """
    Lists schools having a specific topic
    """
    spec_top = {"topics": {"$elemMatch": {"$eq": topic,},},}
    return [i for i in mongo_collection.find(spec_top)]
