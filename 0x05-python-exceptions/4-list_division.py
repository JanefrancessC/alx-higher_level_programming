#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    result = []
    while i < list_length:
        try:
            if type(my_list_1[i]) in [int, float] and type(my_list_2[i]) in [int, float]:
                result.append(my_list_1[i] / my_list_2[i])
            else:
                print("Wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
            break
        i += 1
        finally:
            return result
