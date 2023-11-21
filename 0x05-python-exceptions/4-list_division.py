#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = [0] * list_length
    j = 0
    for i in range(list_length):
        try:
            op = my_list_1[j] / my_list_1[j]
        except (TypeError, ValueError):
            print("wrong type")
            op = 0
        except ZeroDivisionError:
            print("division by 0")
            op = 0
        except IndexError:
            print("out of range")
            op = 0
        finally:
            result[j] = op
            j += 1
    return result
