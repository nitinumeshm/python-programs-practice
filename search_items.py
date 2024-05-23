#!/usr/bin/env python3

## Program to search an element from the given list using binary search method.
## If binary search method fails, we shall use linear search method just to be sure.

import time

## Function to search an element using binary search method
def bin_search(target, array):
    middle = (len(array) - 1) // 2
    
    ## If the country name cannot be searched using binary search method
    if middle < 0:
        print("{} might not exist in the list.".format(target))
        time.sleep(2)
        print("To be a 100% certain that it doesn't exist in the list, performing a linear search instead...")
        time.sleep(2)
        lin_search(key, countries)
        return -1

    ## If it is a perfect match
    elif target.lower() == array[middle].lower():
        print("{} exists in the list...".format(key))
        if target != array[middle]:
            time.sleep(1)
            print("Actual name in the list: {}".format(array[middle]))
        return 0

    ## Choose second half if target greater than middle element
    elif target.lower() > array[middle].lower(): 
        bin_search(target, array[middle+1:])

    ## Choose first half if target less than middle element
    elif target.lower() < array[middle].lower():
        bin_search(target, array[:middle])


## Function to linear search a country name in the given list
def lin_search(target, array):
    for item in array:
        if target.lower() in item.lower():
            print("{} exists in the list.".format(target))
            if target != item:
                time.sleep(2)
                print("Actual name in the list: {}".format(item))
            return 0
    print("{} doesn't exist at all in the list.".format(target))
    return -1

## Initialising the list using a text file
def initialise():
    with open("countries.txt", "r") as f:
        array = f.read().splitlines()
        array.sort() ## It is important to sort the list before proceeding for binary search method
        f.close()
        return array

##### ACTUAL START OF THE PROGRAM #####
key = input("Enter the country name you want to search: ")

print("Searching...")
time.sleep(2)

if key == "":
    print("Invalid!")
else:
    countries = initialise()
    bin_search(key, countries)
