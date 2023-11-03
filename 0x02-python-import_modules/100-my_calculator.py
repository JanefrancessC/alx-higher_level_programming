#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, sub
    import sys
    args = sys.argv
    if len(args) - 1 != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    a = int(args[1])
    op = args[2]
    b = int(args[3])

    if op == '+':
        print('{2} + {1} = {0}'.format(add(a, b), b, a))
    elif op == '-':
        print('{2} - {1} = {0}'.format(sub(a, b), b, a))
    elif op == '*':
        print('{2} * {1} = {0}'.format(mul(a, b), b, a))
    elif op == '/':
        print('{2} / {1} = {0}'.format(div(a, b), b, a))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
