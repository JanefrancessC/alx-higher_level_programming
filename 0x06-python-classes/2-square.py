#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Square """
    def __init__(self, size=0):
        """size is a private attribute for class Square
        Args:
            size (int) with a default value of 0
        Raises:
            TypeError if size is not an integer
            ValueError if size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
