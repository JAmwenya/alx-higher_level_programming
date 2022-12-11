#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if digit > 5:
    print(f"last digit o {number:d} is {number:d} and is greater than 5", end="")
elif number == 0:
    print(f"last digit of {number:d} is {number:d} and is 0", end="")
elif number < 6:
    print(f"last digit of {number:d} is {number:d} and is less than 6 and not 0", end="")
elif number != 0:
    print(f"last digit of {number:d} is {number:d} and is less than 6 and not 0", end="")
