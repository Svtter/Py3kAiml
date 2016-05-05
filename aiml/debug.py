#!/usr/bin/env python
# coding: utf-8

import similarity

__author__ = 'svtter'


def debug(func):
    def wrapper(*args, **kw):
        try:
            return func(*args, **kw)
        except Exception as e:
            print("error in ", func.__name__)
            print("Error is: ", e)
            return None
    return wrapper


@debug
def hello():
    print(1/0)


if __name__ == '__main__':
    hello()
    similarity.Primitive.init()
    print(similarity.Primitive.similar_word("FUCK", "你最近吃啥来"))
    print(similarity.Primitive.similar_word("你好", "你好"))
