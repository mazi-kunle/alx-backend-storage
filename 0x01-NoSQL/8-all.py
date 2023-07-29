#!/usr/bin/env python3
'''This is a module'''

import pymongo


def list_all(mongo_collection):
    '''
    A function that lists all documents in a collection
    '''
    documents = mongo_collection.find()
    return [i for i in documents]
