#!/usr/bin/env python3

## Program to create fibonacci series

## The program prompts the user to enter a number. 
## Using this input, it generates a Fibonacci series up to that specified number.

def fibo(num):
  if num <= 0:
    print("Are you an IDIOT?? I said a number greater than ZERO!")                                                         
    print("What part of 'greater than ZERO' didn't you understand??")
  elif num == 1:
    print("Fibonacci Series: {}".format(num))
  else:
    list = []
    for i in range(num):
      if i == 0:
        list.append(0)
      elif i == 1:
        list.append(1)
      else:
        list.append(list[i-1] + list[i-2])
    print("Fibonacci Series: {}".format(list))

print("FIBONACCI SERIES")
x = int(input("Enter a number greater than ZERO: "))

fibo(x)
