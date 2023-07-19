#!/usr/bin/env python3
""" Tools for request caching and tracking """

import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.redis()


def data_cacher(methos: Callable) -> Callable:
    """ Caches output of fetched data """
    @wraps(method)
    def invoker(url) -> str:
        """Wrapper function for caching output"""
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utl-8')
        result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    """Returns content of a URL after caching the request's
    response, and tracking the request"""
    return requests.get(url).text
