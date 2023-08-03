#!/usr/bin/env python3
'''This is a module'''

import redis
from typing import Union, Callable, Any
import uuid
from functools import wraps


def count_calls(
        method: Callable[[Any, Union[str, bytes, int, float]], str]
        ) -> Callable[[Any], Any]:
    '''
    A decorator
    '''
    @wraps(method)
    def wrapper(self, data) -> Any:
        '''A wrapper function that calls the function after
        incrementing the call counter
        '''
        self._redis.incr(method.__qualname__)
        return method(self, data)

    return wrapper


class Cache:
    '''
    A cache class
    '''
    def __init__(self) -> None:
        '''An init function'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        takes a data argument and returns a string
        '''
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get(
            self,
            key: str,
            fn: Callable = None
            ) -> Union[str, bytes, int, float]:
        '''
         a get method that take a key string argument and
         an optional Callable argument named fn. This callable
         will be used to convert the data back to the desired format.
        '''
        ans = self._redis.get(key)

        if ans and fn is not None:
            return fn(ans)

        return ans

    def get_str(self, key: str) -> str:
        '''
        parametrize Cache.get to a str
        '''
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        '''
        parametrize Cache.get to an int
        '''
        return self.get(key, lambda x: int(x))
