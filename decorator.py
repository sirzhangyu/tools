#coding=utf-8

import dbus
import json

from logger import logger


def singleton(cls):
    instances = dict()
    def _sigleton(*args, **kargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kargs)
        return instances[cls]
    return _sigleton


def ignore_error(err):
    def _error(func):
        def wrapper(*args, **kargs):
            try:
                return func(*args, **kargs)
            except err as e:
                logger.warning(e)
        return wrapper
    return _error


def log_error(func):
    def wrapper(*args, **kargs):
        try:
            return func(*args, **kargs)
        except Exception as e:
            logger.error(e.message)
            raise e
    return wrapper


# change a value from dbus type to python type
def dbus_type2python_type(func):
    def wrapper(*args, **kargs):
        ret = func(*args, **kargs)
        if type(ret) is dbus.String:
            return str(ret)
        elif type(ret) is dbus.UTF8String:
            return str(ret)
        elif type(ret) is dbus.Int32:
            return int(ret)
        elif type(ret) is dbus.Boolean:
            return bool(ret)
        elif not ret:
            raise TypeError("Response is None")
        else:
            return ret
    return wrapper
