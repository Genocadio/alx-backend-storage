#!/usr/bin/env python3
"""ses the requests module to obtain the HTML content of a particular URL"""

import requests
import time
from functools import wraps


def cache_decorator(exp_t):
    """Decorator that takes an integer argument named expiration time"""
    cache = {}

    def decorator(func):
        """Decorator that takes a function and returns a wrapped function"""
        @wraps(func)
        def wrapper(url):
            """Wrapper function"""
            if url in cache and time.time() - cache[url]['timestamp'] < exp_t:
                return cache[url]['content']

            response = requests.get(url)
            content = response.text

            cache[url] = {
                'content': content,
                'timestamp': time.time()
            }

            return content

        return wrapper

    return decorator


@cache_decorator(exp_t=10)
def get_page(url):
    """Function that returns the HTML content of a particular URL"""
    response = requests.get(url)
    return response.text
