#!/usr/bin/env python3
"""Write a Python script that provides some stats about Nginx
logs stored in MongoDB:
Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the number of documents with the method =
["GET", "POST", "PUT", "PATCH", "DELETE"] in this order
(see example below - warning: it’s a tabulation before each line)
one line with the number of documents with:
method=GET
path=/status
You can use this dump as data sample: dump.zip
"""


import pymongo


def count_logs(collection):
    """Count number of logs"""
    return collection.count_documents({})


def count_methods(collection):
    """Count number of logs with different HTTP methods"""
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    counts = []
    for method in methods:
        count = collection.count_documents({"method": method})
        counts.append(count)
    return counts


def get_status_check(collection):
    """Count number of logs with method=GET and path=/status"""
    return collection.count_documents({"method": "GET", "path": "/status"})


if __name__ == "__main__":
    # Create connection to MongoDB
    client = pymongo.MongoClient()
    # Choose database and collection
    db = client.logs
    collection = db.nginx
    # Count number of logs
    num_logs = count_logs(collection)
    print(f"{num_logs} logs")
    # Count number of logs with each HTTP method
    methods_counts = count_methods(collection)
    print("Methods:")
    print(f"\tmethod GET: {methods_counts[0]}")
    print(f"\tmethod POST: {methods_counts[1]}")
    print(f"\tmethod PUT: {methods_counts[2]}")
    print(f"\tmethod PATCH: {methods_counts[3]}")
    print(f"\tmethod DELETE: {methods_counts[4]}")
    # Count number of logs with method=GET and path=/status
    num_status_checks = get_status_check(collection)
    print(f"{num_status_checks} status check")
