#!/usr/bin/env python3
""" Tools for request caching and tracking """

import redis
import requests
from functools import wraps
from typing import Callable


def data_cacher(fn: Callable) -> Callable:
    """ Caches output of fetched data """
    @wraps(fn)
    def invoker(url: str) -> str:
        """Wrapper function for caching output"""
        client = redis.Redis()
        client.incr(f'count:{url}')
        result = client.get(f'{url}')
        if result:
            return result.decode('utf-8')
        response = fn(url)
        client.setex(f'{url}', response, 10)
        return response
    return invoker


@data_cacher
def get_page(url: str) -> str:
    """Returns content of a URL after caching the request's
    response, and tracking the request"""
    response = requests.get(url, timeout=10)
    return response.text
