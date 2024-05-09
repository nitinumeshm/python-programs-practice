#!/usr/bin/env python3

## Program to reverse the list elements

## Function to reverse the elements in the list
def reverse(list):
  length = len(list)
  reverse_list = []
  while length != 0:
    reverse_list.append(list[length - 1])
    length = length - 1
  print("Reverse List Elements: {}".format(reverse_list))

## Initialising a list
n = int(input("Enter the number of elements in your list: "))
list = []
for i in range(n):
  x = input("Enter element number {}: ".format(i))
  list.append(x)

## Call to function reverse()
reverse(list)
