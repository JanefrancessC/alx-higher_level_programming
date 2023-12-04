#!/usr/bin/python3
"""class MyList that inherits from parent class list"""
class MyList(list):

    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
