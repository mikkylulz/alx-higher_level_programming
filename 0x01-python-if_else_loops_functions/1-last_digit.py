#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = repr(number)
last_digit = num_str[-1]
las = int(last_digit)
print(f"Last digit of {number} is {las}")
if las > 5:
    print(f"{las} and is greater than 5")
elif las == 0:
    print(f"{las} and is 0")
elif (las > 6) and (not 0):
    print(f"{las} and is less than 6 and not 0")
