#!/usr/bin/env python3
'''task 11 module'''

import pymongo


# def schools_by_topic(mongo_collection, topic):
#     '''
#     a Python function that returns the list of school having a specific topic
#     '''
#     lst = []
#     for i in mongo_collection.find():
#         if topic in i.get('topics', ''):
#             lst.append(i)

#     return lst


def schools_by_topic(mongo_collection, topic):
    '''
    a Python function that returns the list of school having a specific topic
    '''
    lst = []
    # ans = mongo_collection.find({'topics': {'$elemMatch': {'$eq': topic}}})
    ans = mongo_collection.find({'topics': topic})

    return [i for i in ans]
