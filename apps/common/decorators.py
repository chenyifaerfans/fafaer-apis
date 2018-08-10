# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/10 8:54'


def debug(func):
    def wrapper(*args, **kwargs):
        print("[DEBUG]: enter function {func}()".format(func=func.__name__))
        return func(*args, **kwargs)

    return wrapper


def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(level=level, func=func.__name__))
            return func(*args, **kwargs)

        return inner_wrapper

    return wrapper


class Log(object):
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, *args, **kwargs):
        def wrapper(func):
            print("[{level}]: enter function {func}()".format(level=self.level, func=func.__name__))
            return func(*args, **kwargs)

        return wrapper
