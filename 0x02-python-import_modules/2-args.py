#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    argc = len(args) - 1
    arguments = "argument" if argc == 1 else "arguments"

    if argc == 0:
        print('0 {}.'.format(arguments))
    else:
        print('{} {}:'.format(argc, arguments))
        for i in range(1, len(args)):
            print('{}: {}'.format(i, args[i]))
