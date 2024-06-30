#!/usr/bin/env python3

## PROGRAM to check whether the given number is a prime number or not

import time

print("***WELCOME TO PRIME NUMBER CHECKER***\n")
time.sleep(1)
num = int(input("Enter a number: "))
time.sleep(1)

if num == 0:
    print("{} is NOT PRIME.".format(num))
elif num == 1 or num == 2:
    print("{} is PRIME!".format(num))
elif num > 2:
    counter = list(range(2, num))
    factors = []
    for i in counter:
        if num % i == 0:
            factors.append(i)
    if len(factors) == 0:
        print("{} is PRIME!".format(num))
    else:
        print("{} is NOT PRIME".format(num))
        time.sleep(1)
        print("Factors of {} are: {}".format(num, factors))
