#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_reversed = list(reversed(my_list))
    for i in list_reversed:
        print("{:d}".format(i))
