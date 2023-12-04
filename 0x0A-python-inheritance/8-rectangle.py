#!/usr/bin/python3
"""Define a BaseGeometry class"""


class BaseGeometry:
    """raises an exception"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates input value
        Args:
        name (string) - user input
        value (int) - value to validate
        Raises:
            TypeError: if value not an integer
            ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry class"""

    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
