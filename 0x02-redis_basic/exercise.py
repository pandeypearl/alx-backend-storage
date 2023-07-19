#!/usr/bin/env python3
""" Writting strings to Redis """

from typing import Union, Optional, Union
import redis
import uuid


class Cache:
    """ Cache class """
    def __init__(self):
        """ Constructor function """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generates a random key """
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: Optional[Callable] = None):
        """ Converst data back to the desired format """
        val = self._redis.get(key)
        return val if not fn else fn(val)

    def get_str(self, key):
        """ Parametrize Cache.get with
        correct(str) conversion function """
        return self.get(key, str)

    def get_int(self, key):
        """ Parametrize Cache.get with
        correct(int) conversion function """
        return self.get(key, int)
