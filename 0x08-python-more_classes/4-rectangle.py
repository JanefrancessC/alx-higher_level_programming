#!/usr/bin/python3
"""Module: defines a Rectangle class"""


class Rectangle:
    """A Rectangle class"""
    def __init__(self, width=0, height=0):
        """width and height are private attributes for class Rectangle
        Args:
            width (int) with a default value of 0
            height (int) with a default value of 0
        Raises:
            TypeError if width/height is not an integer
            ValueError if width/height < 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self .height == 0:
            return ""
        res = ""
        for i in range(self.height):
            for j in range(self.width):
                res += "#"
            if i < self.height - 1:
                res += "\n"
        return res

    def __repl__(self):
        res = f"Rectangle({self.width}, {self.height})"
        return res
