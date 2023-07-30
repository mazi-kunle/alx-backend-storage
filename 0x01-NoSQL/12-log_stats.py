#!/usr/bin/env python3
'''task 12 module'''

import pymongo
from pymongo import MongoClient


def getDetails(mongoCollection):
    '''
    Return log summary
    '''
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    count = mongoCollection.count_documents({})
    print(f'{count} logs')
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


if __name__ == '__main__':
    client = MongoClient('localhost', 27017)
    db = client['logs']
    collection = db['nginx']
    getDetails(collection)
