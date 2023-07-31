#!/usr/bin/env python3
'''task 14 module'''

import pymongo


def top_students(mongo_collection):
    '''
    a Python function that returns all students sorted by average score
    '''
    all_students = mongo_collection.aggregate([
        {
            '$project': {
                'name': '$name',
                'averageScore': {'$avg': '$topics.score'}
            }
        },
        {
            '$sort': {'averageScore': -1}
        }
    ])
    return all_students
