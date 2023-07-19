#!/usr/bin/env python3
""" Tools for request caching and tracking """

import redis
import requests
from functools import wraps
from typing import Dict
import time


def data_cacher(exp_time: int):
    """ Caches output of fetched data """
    def decorator(func):
        result = {}

        @wraps(func)
        def invoker(url):
            """Wrapper function for caching output"""
            if url in result and time.time() - \
                    result[url]['timestamp'] < exp_time:
                result[url]['count'] += 1
                return result[url]['content']

            content = func(url)
            result[url] = {
                'content': content,
                'timestamp': time.time(),
                'count': 1
            }
            return result

        return invoker

    return decorator


@data_cacher(exp_time=10)
def get_page(url: str) -> str:
    """Returns content of a URL after caching the request's
    response, and tracking the request"""
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    url = ('http://slowwly.robertomurray.co.uk/delay/1000/url')
    for _ in range(5):
        print(get_page(url))
        time.sleep(3)
