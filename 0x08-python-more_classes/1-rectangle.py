#!/usr/bin/python3
"""A module that defines a Rectangle class"""


class Rectangle:
    """class Rectangle with private instance attributes"""
    def __init__(self, width=0, height=0):
        """ width and height are private attributes of Rectangle
        Args:
        width (int) - default value is 0
        height (int) - default value = 0

        Raises:
        TypeError - width/height  must be an integer
        ValueError - width/height must be >= 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """set width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
