#!/usr/bin/python3
"""
returns True if the object is exactly
an instance of the specified class ;
otherwise False
"""


def is_same_class(obj, a_class):
    """
    Args:
    obj - object to check
    a_class -  specified class
    Return: True or False
    """
    return type(obj) == a_class
