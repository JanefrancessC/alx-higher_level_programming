#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    result = add(a, b)
print('{2} + {1} = {0}'.format(result, b, a))
