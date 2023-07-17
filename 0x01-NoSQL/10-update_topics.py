#!/usr/bin/env python3
""" Defines update_topics """


def update_topics(mongo_collection, name, topics):
    """
    Changes all topivs of school document based on the name
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
