#!/usr/bin/env python3

## Program to 
##   1. search an element in the array
##   2. sort the array

## Function to search an element in the array
def search_element(arr, k):
  counter = 0
  for i in arr:
    if k == i:
      print("{} is present in the array at position {}".format(k, counter))
      return 1
    counter = counter + 1
  return 0

## Function to sort the array (Bubble Sort)
def sort_array(arr):
  for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
      if arr[j] > arr[j+1]:
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp
  print("Sorted Array (in ascending order): {}".format(arr))

##Initialising the array
n = int(input("Enter the number of elements in your array: "))
arr = []
for i in range(n):
  x = int(input("Enter Element {}: ".format(i)))
  arr.append(x)

## Call to functions search_element() and sort_array()
k = int(input("Enter the element you to find: "))
if search_element(arr, k) == 0:
  print("Element {} not found in your array.".format(k))

sort_array(arr)


