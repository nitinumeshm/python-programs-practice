#!/usr/bin/env python3

## Program to swap first and last elements of the list

## Function to swap positions of the first and last elements in the given list
def swap_elements(list, n):
  list[0], list[n-1] = list[n-1], list[0]
  print("List after swapping positions of first and last elements: {}".format(list))

## Initialising the list
n = int(input("Enter number of elements in your list: "))
list = []
for i in range(n):
  x = input("Enter Element {}: ".format(i))
  list.append(x)
print("Original List: {}".format(list))

## Call to function swap_elements()
if len(list) <= 1:
  print("Cannot swap as there are less than 2 elements in your list.")
else:
  swap_elements(list, n)
