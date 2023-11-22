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

    def area(self):
        """
        Returns an int - area of a square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Retrieves size """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets position of the square

        Args:
        value (tuple): new position of square

        Raises:
        TypeError if tuple is not 2 integers
        """
        if not isinstance(value, tuple) or len(value) != 2 \
                or any(not isinstance(n, int)) \
                or n < 1 for n in value:
                    raise TypeError(
                            "position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        prints in stdout the square with the character #
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for j in range(self.size):
                print("f{' ' * self.position[0]}#{'#' * (self.size - 1)}")
