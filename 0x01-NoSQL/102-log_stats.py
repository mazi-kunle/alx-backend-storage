#!/usr/bin/env python3
'''task 15 module'''

import pymongo
from pymongo import MongoClient


def getDetails(mongoCollection):
    '''
    Return log summary
    '''
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    count = mongoCollection.count_documents({})
    print(f'{count} logs')
    print('Methods:')
    for i in method:
        i_count = mongoCollection.count_documents(
            {
                "method": i
            }
        )
        print(f'\tmethod {i}: {i_count}')

    status_count = mongoCollection.count_documents(
        {
            "path": "/status",
        }
    )
    print(f'{status_count} status check')

    query = mongoCollection.aggregate([
        {
            '$group': {
                '_id': '$ip',
                'count': {'$sum': 1}
            }
        },
        {
            '$sort': {'count': -1}
        },
        {
            '$limit': 10
        }

    ])
    print('IPs:')
    for i in query:
        print(f"\t{i['_id']}: {i['count']}")


def run():
    '''
    run the main program
    '''
    client = MongoClient('localhost', 27017)
    db = client['logs']
    collection = db['nginx']
    getDetails(collection)


if __name__ == '__main__':
    run()
