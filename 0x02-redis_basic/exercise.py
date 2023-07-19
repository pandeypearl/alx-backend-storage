#!/usr/bin/env python3
""" Writting strings to Redis """

from typing import Union, Optional, Union, Any, Callable
import redis
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Tracks number of calls made
    to a method in a Cache class"""
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        """Invokes the given method after
        incrementing its call counter"""
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return invoker


def call_history(method: Callable) -> Callable:
    """Tracks the call history of a method in
    Cache class"""
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        """returns the method's output after
        atoring it's inputs and output"""
        input_key = '{}:inputs'.format(method.__qualname__)
        output_key = '{}:outputs'.format(method.__qualname__)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(output_key, output)
        return output
    return invoker


def replay(fn: Callable) -> None:
    """Displays the call history of Cache class' method"""
    if fn is None or not hasattr(fn, '__self__'):
        return
    redis_store = getattr(fn.__self__, '_redis', None)
    if not isinstance(redis_store, redis.Redis):
        return
    func_name = fn.__qualname__
    input_key = '{}:inputs'.format(func_name)
    output_key = '{}:outputs'.format(func_name)
    func_call_count = 0
    if redis_store.exists(func_name) != 0:
        func_call_count = int(redis_store.get(func_name))
    print('{} was called {} times:'.format(func_name, func_call_count))
    func_inputs = redis_store.lrange(input_key, 0, -1)
    func_outputs = redis_store.lrange(output_key, 0, -1)
    for func_input, func_output in zip(func_inputs, func_outputs):
        print('{}(*{}) -> {}'.format(
            func_name,
            func_input.decode("utf-8"),
            func_output,
        ))


class Cache:
    """ Cache class """
    def __init__(self):
        """ Constructor function """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
