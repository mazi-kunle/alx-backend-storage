#!/usr/bin/env python3
'''This is a module'''

import redis
from typing import Union
import uuid


class Cache:
    '''
    A cache class
    '''
    def __init__(self) -> None:
        '''An init function'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        takes a data argument and returns a string
        '''
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id
