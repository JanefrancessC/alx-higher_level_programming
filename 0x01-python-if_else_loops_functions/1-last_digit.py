#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

def last_digit(n):
    if n < 0:
        return n % -10
    else:
        return n % 10
lastDigit = last_digit(number)

if lastDigit == 0:
    print(f"Last digit of {number} is {lastDigit} and is 0")
elif lastDigit > 5:
    print(f"Last digit of {number} is {lastDigit} and is greater than 5")
elif lastDigit < 6 and lastDigit != 0:
    print(f"Last digit of {number} is {lastDigit} and is less than 6 and not 0")
