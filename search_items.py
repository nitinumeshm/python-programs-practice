#!/usr/bin/env python3

## Program to search an element from the given list using binary search method.
## If binary search method fails, we shall use linear search method just to be sure.

import time

## Function to search an element using binary search method
def bin_search(target, array):
    middle = (len(array) - 1) // 2
    
    ## If the country name cannot be searched using binary search method
    if middle < 0:
        print("{} might not exist in the list.\n".format(target))
        time.sleep(2)
        print("To be a 100% certain that it doesn't exist in the list, performing a linear search instead...\n")
        time.sleep(2)
        return -1

    ## If it is a perfect match
    elif target.lower() == array[middle].lower():
        print("{} exists in the list...\n".format(target))
        if target != array[middle]:
            time.sleep(2)
            print("Actual name in the list: {}\n".format(array[middle]))
        return 0

    ## Choose second half if target greater than middle element
    elif target.lower() > array[middle].lower(): 
        if bin_search(target, array[middle+1:]) == -1:
            return -1

    ## Choose first half if target less than middle element
    elif target.lower() < array[middle].lower():
        if bin_search(target, array[:middle]) == -1:
            return -1


## Function to linear search a country name in the given list
def lin_search(target, array):
    temp = []
    
    for item in array: 
        if target.lower() in item.lower():
            if target != item:
                temp.append(item)

    if len(temp) == 0:
        print("{} doesn't exist at all in the list.\n".format(target))
        return -1

    elif len(temp) == 1:
        print("I think you're searching for {}".format(temp[0]))
        return 0

    elif len(temp) > 1:
        print("The country name that you're searching for is one of the following...\n")
        time.sleep(2)
        counter = 1
        for element in temp:
            print("{}: {}".format(counter, element))
            counter = counter + 1
            time.sleep(2)
        print("\nTHAT's IT!!!\n")
        return 1

## Initialising the list using a text file
def initialise():
    with open("countries.txt", "r") as f:
        array = f.read().splitlines()
        array.sort() ## It is important to sort the list before proceeding for binary search method
        f.close()
        return array

##### ACTUAL START OF THE PROGRAM #####
key = input("Enter the country name you want to search: ")

print("\nSearching...")
time.sleep(2)

if key == "":
    print("\nInvalid!")
else:
    countries = initialise()
    if bin_search(key, countries) == -1:
        countries = initialise()
        lin_search(key, countries)
