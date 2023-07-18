#!/usr/bin/env python3
""" Provides stats about Nginx logs restored in MongoDB """
import pymongo as pm
db = pm.MongoClient()
mydb = db["logs"]
mycol = mydb["nginx"]


if __name__ == "__main__":
    get_get = mycol.count_documents({"method": "GET"})
    get_post = mycol.count_documents({"method": "POST"})
    get_put = mycol.count_documents({"method": "PUT"})
    get_patch = mycol.count_documents({"method": "PATCH"})
    get_delete = mycol.count_documents({"method": "DELETE"})
    get_total = mycol.count_documents({})
    get_status = mycol.count_documents({"method": "GET", "path": "/status"})

    print("{} logs".format(get_total))
    print("Methods:\n\tmethod GET: {}\n\tmethod POST: {}\n\tmethod PUT: {}\n\tmethod PATCH: {}\n\tmethod DELETE: {}".format(
                   get_get, get_post, get_put, get_patch, get_delete))
    print("{} status check".format(get_status))
'''
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    x = len(list(nginx_collection.find()))
    print(x, "logs\nMethods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for meth in methods:
        print(
            "\tmethod {}: {}".format(
                meth, len(list(nginx_collection.find({"method": meth})))
                )
            )
        print(
            "{} status check".format(
                len(list(
                    nginx_collection.find({"method": "GET", "path": "/status"})
                    ))
                )
            )
'''
