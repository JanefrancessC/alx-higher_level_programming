#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            op = 0
            op = my_list_1[i] / my_list_1[i]
        except TypeError as e:
            print("wrong type")
        except ZeroDivisionError as e:
            print("division by 0")
        except IndexError as e:
            print("out of range")
        finally:
            result.append(op)
    return result
