#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date : 2019-11-12 19:02:46
__author__ = 'luozaibo'


import wrapt
import time
import inspect
import json


def mylog(level):
    @wrapt.decorator
    def wrapper(wrapped, isinstance, args, kwargs):
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(t)
        print(f'开始运行{wrapped.__name__}，日志级别是: {level}')
        return wrapped(*args, **kwargs)
    return wrapper


@wrapt.decorator
def universal(wrapped, instance, args, kwargs):
    if instance is None:
        if inspect.isclass(wrapped):
            # Decorator was applied to a class.
            return wrapped(*args, **kwargs)
        else:
            t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            print(t)
            print(f'开始运行: {wrapped.__name__}')
            # Decorator was applied to a function or staticmethod.
            return wrapped(*args, **kwargs)
    else:
        if inspect.isclass(instance):
            # Decorator was applied to a classmethod.
            return wrapped(*args, **kwargs)
        else:
            # Decorator was applied to an instancemethod.
            return wrapped(*args, **kwargs)

# json输出装饰器
@wrapt.decorator
def output_json(wrapped, isinstance, args, kwargs):
    result = wrapped(*args, **kwargs)
    return print(json.dumps(result))

# @mylog(level='warning')
@universal
def myfunc(a, b):
    sum = a + b
    print(sum)

@output_json
def json_demo():
    json_str = {'hello': 'world'}
    return json_str


if __name__ == "__main__":
    # myfunc(a=3, b=10)
    json_demo()