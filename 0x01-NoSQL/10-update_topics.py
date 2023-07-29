#!/usr/bin/env python3
'''task 10 module'''

import pymongo


def update_topics(mongo_collection, name, topics):
    '''
    a Python function that changes all topics of
    a school document based on the name
    '''
    query = {'name': name}
    newval = {'$set': {'topics': topics}}
    res = mongo_collection.update_many(query, newval)
