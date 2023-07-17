# 0x01. NoSQL
Introduction to NoSQL and MongoDB covering the following topics and concepts:

   + What NoSQL means
   + What is difference between SQL and NoSQL
   + What is ACID
   + What is a document storage
   + What are NoSQL types
   + What are benefits of a NoSQL database
   + How to query information from a NoSQL database
   + How to insert/update/delete information from a NoSQL database
   + How to use MongoDB

## Tasks

### 0. List all databases
Write a script that lists all databases in MongoDB.

file: [0-list_databases](0-list_databases)


### 1. Create a database
Write a script that creates or uses the database my_db

file: [1-use_or_create_database](1-use_or_create_database)


### 2. Insert document
Write a script that inserts a document in the collection school:

   + The document must have one attribute name with value “Holberton school”
   + The database name will be passed as option of mongo command

file: [2-insert](2-insert)


### 3. All documents
Write a script that lists all documents in the collection school:

   + The database name will be passed as option of mongo command

file: [3-all](3-all)


### 4. All matches
Write a script that lists all documents with name="Holberton school" in the collection school:

   + The database name will be passed as option of mongo command

file: [4-match](4-match)


### 5. Count
Write a script that displays the number of documents in the collection school:

   + The database name will be passed as option of mongo command

file: [5-count](5-count)


### 6. Update
Write a script that adds a new attribute to a document in the collection school:

   + The script should update only document with name="Holberton school" (all of them)
   + The update should add the attribute address with the value “972 Mission street”
   + The database name will be passed as option of mongo command

file: [6-update](6-update)


### 7. Delete by match
Write a script that deletes all documents with name="Holberton school" in the collection school:

   + The database name will be passed as option of mongo command

file: [7-delete](7-delete)


### 8. List all documents in Python
Write a Python function that lists all documents in a collection:

   + Prototype: def list_all(mongo_collection):
   + Return an empty list if no document in the collection
   + mongo_collection will be the pymongo collection object

file: [8-all.py](8-all.py)
test file: [tests/8-main.py](tests/8-main.py)


### 9. Insert a document in Python
Write a Python function that inserts a new document in a collection based on kwargs:

   + Prototype: `def insert_school(mongo_collection, **kwargs):`
   + mongo_collection will be the pymongo collection object
   + Returns the new _id

file: [9-insert_school.py](9-insert_school.py)
test file: [tests/9-main.py](tests/9-main.py)


### 10. Change school topics
Write a Python function that changes all topics of a school document based on the name:

   + Prototype: `def update_topics(mongo_collection, name, topics):`
   + mongo_collection will be the pymongo collection object
   + name (string) will be the school name to update
   + topics (list of strings) will be the list of topics approached in the school

file: [10-update_topics.py](10-update_topics.py)
test file: [tests/10-main.py](tests/10-main.py)


### 11. Where can I learn Python?
Write a Python function that returns the list of school having a specific topic:

   + Prototype: def schools_by_topic(mongo_collection, topic):
   + mongo_collection will be the pymongo collection object
   + topic (string) will be topic searched

file: [11-schools_by_topic.py](11-schools_by_topic.py)
test file: [tests/11-main.py](tests/11-main.py)


### 12. Log stats
Write a Python script that provides some stats about Nginx logs stored in MongoDB:

   + Database: logs
   + Collection: nginx
   + Display (same as the example):
       + first line: x logs where x is the number of documents in this collection
       + second line: Methods:
       + 5 lines with the number of documents with the method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order (see example below - warning: it’s a tabulation before each line)
        one line with the number of documents with:
           + method=GET
           + path=/status

You can use this dump as data sample: [dump.zip](https://intranet.alxswe.com/rltoken/0szbpslKvH3RqKb_2HUeoQ)

file: [12-log_stats.py](12-log_stats.py)


## Advanced Tasks

### 13. Regex filter
Write a script that lists all documents with name starting by Holberton in the collection school:

   + The database name will be passed as option of mongo command

file: [100-find](100-find)


### 14. Top students
Write a Python function that returns all students sorted by average score:

   + Prototype: def top_students(mongo_collection):
   + mongo_collection will be the pymongo collection object
   + The top must be ordered
   + The average score must be part of each item returns with key = averageScore

file: [101-students.py](101-students.py)


### 15. Log stats - new version
Improve 12-log_stats.py by adding the top 10 of the most present IPs in the collection nginx of the database logs:

   + The IPs top must be sorted (like the example below)

file: [102-log_stats.py](102-log_stats.py)
