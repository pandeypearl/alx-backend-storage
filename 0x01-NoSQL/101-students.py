#!/usr/bin/env python3
""" Defines top_students """


def top_students(mongo_collection):
    """
    Prints all studetns sorted by average score
    """
    ave = mongo_collection.aggregate(
        [{"$project": {"_id": 1, "name": 1,
                       "averageScore": {
                           "$avg": {
                               "$avg": "$topics.score", },
                           }, "topics": 1, }, },
            {"$sort": {"averageScore": -1}, }, ])
    return ave
