#!/usr/bin/env python3

## Program to calculate the sum of array elements

## Function that calculates the sum of array elements

def sum_array(array):
  sum = 0
  for i in array:
    sum = sum + i
  print("Sum of array elements: {}".format(sum))

## This part of the code initialises the array by entering user input
n = int(input("Enter number of elements: "))
array = []
for i in range(n):
  x = int(input("Enter Element {}: ".format(i)))
  array.append(x)

## Call to function sum_array()
sum_array(array)
