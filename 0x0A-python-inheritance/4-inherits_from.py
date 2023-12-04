#!/usr/bin/python3
"""
checks if the object is an instance of a class that
inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    obj (Any) - object to check
    a_class - specified class
    Return: True or False
    """
    return issubclass(type(obj), a_class)
