#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastd = number % 10
if number < 0:
    lastd = (-1 * number) % 10
    lastd = -lastd
if lastd > 5:
    print(f"Last digit of {number} is {lastd} is greater then 5")
elif lastd == 0:
    print(f"Last digit of {number} is {lastd} is zero")
else:
    print(f"Last digit of {number} is {lastd} is less then 6 and not 0")
