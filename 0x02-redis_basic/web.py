#!/usr/bin/env python3
""" Tools for request caching and tracking """

import redis
import requests
from functools import wraps
from typing import Callable


redis_ = redis.Redis()
""" Module-level Redis instance """


def data_cacher(method: Callable) -> Callable:
    """ Caches output of fetched data """
    @wraps(method)
    def invoker(url):
        """Wrapper function for caching output"""
        redis_.incr(f'count:{url}')
        cached_result = redis_.get(f'cached:{url}'}
        if cached_result:
            return cached_result.decode('utf-8')
        result = method(url)
       # redis_store.set(f'count:{url}', 0)
        redis_.setex(f'cached:{url}', 10, result)
        return result

    return invoker


@data_cacher
def get_page(url: str) -> str:
    """Returns content of a URL after caching the request's
    response, and tracking the request"""
    req = requests.get(url)
    return req.text
