#!/usr/bin/python3
"""returns the list of available attributes and methods of an object"""


def lookup(obj):
    """ returns a list object"""
    return list(dir(obj))
