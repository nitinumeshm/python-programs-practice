#!/usr/bin/env python3

## Program to search an element from the given list using binary search method

## Function to search an element using binary search method
def search(key, countries):
    middle = (len(countries) - 1) // 2

    if key == "":
        print("Invalid!")
        return False

    elif key == countries[middle]:
        print("{} exists in the list.".format(key))
        return True

    ## Choose second half if key greater than middle element
    elif key > countries[middle]: 
        search(key, countries[middle+1:])

    ## Choose first half if key less than middle element
    elif key < countries[middle]:
        search(key, countries[:middle])

    else:
        print("{} doesn't not exist in the list.".format(key))
        return False


## Initialising the list using a text file
with open("countries.txt", "r") as f:
    countries = f.read().splitlines()
    countries.sort() ## It is important to sort the list before proceeding for binary search method

key = input("Enter the country name you want to search: ")

## Call to search function
search(key, countries)
