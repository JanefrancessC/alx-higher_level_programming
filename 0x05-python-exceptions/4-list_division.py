#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = [0] * list_length
    j = 0
    for i in range(list_length):
        try:
            op = my_list_1[j] / my_list_1[j]
        except (TypeError, ValueError):
            op = 0
            print("wrong type")
        except ZeroDivisionError:
            op = 0
            print("division by 0")
        except IndexError:
            op = 0
            print("out of range")
        finally:
            result[j] = op
            j += 1
    return result
