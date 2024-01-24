#!/usr/bin/env python3
"""redis module"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def replay(method: Callable):
    """Replay decorator"""
    key = method.__qualname__
    r = redis.Redis()

    inputs = r.lrange("{}:inputs".format(key), 0, -1)
    outputs = r.lrange("{}:outputs".format(key), 0, -1)
    calls = len(inputs)
    times = 'times'
    if calls == 1:
        times = 'time'
    out = '{} was called {} {}:'.format(key, calls, times)
    print(out)
    for i, o in zip(inputs, outputs):
        out = '{}(*{}) -> {}'.format(key, i.decode('utf-8'),
                                     o.decode('utf-8'))
        print(out)


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        self._redis.rpush("{}:inputs".format(key), str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush("{}:outputs".format(key), result)
        return result
    return wrapper


def count_calls(method: Callable) -> Callable:
    """Decorator count calls"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Cache class"""
    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store method"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str, fn: Optional[callable] = None) -> Union[str,
                                                              bytes,
                                                              int, float]:
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
