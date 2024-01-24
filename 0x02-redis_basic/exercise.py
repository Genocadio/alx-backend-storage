#!/usr/bin/env python3
"""redis module"""

import redis
import uuid
from typing import Union


def count_calls(method: callable) -> callable:
    """Decorator count calls"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        key_m = method.__qualname__
        self._redis.incr(key_m)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Cache class"""
    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store method"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: callable = None) -> Union[str,
                                                          bytes, int, float]:
        """Get method"""
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """Get string method"""
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        return self.get(key, int)
