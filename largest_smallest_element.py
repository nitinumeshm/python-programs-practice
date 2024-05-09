#!/usr/bin/env python3

## Program to find out the largest and smallest element in the array

## Function to find the largest element
def largest(array):
  max = array[0]
  for i in array:
    if max < i:
      max = i
  print("Largest Element in the array: {}".format(max))

## Function to find the smallest element
def smallest(array):
  min = array[0]
  for i in array:
    if min > i:
      min = i
  print("Smallest Element in the array: {}".format(min))

## Initialising the array
n = int(input("Enter the number of elements in the array: "))
array = []
for i in range(n):
  x = int(input("Enter element {}: ".format(i)))
  array.append(x)

## Call to functions largest() and smallest()
largest(array)
smallest(array)
