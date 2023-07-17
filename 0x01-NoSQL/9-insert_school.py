#!/usr/bin/env python3
""" Defines insert_school """


def insert_school(mongo_collection, **kwargs):
    """
    Inserts new document in collection school
    based on kwargs
    """
    md = mongo_collection.insert_one(kwargs)
    return md.inserted_id
