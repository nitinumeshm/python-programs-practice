#!/usr/bin/env python3

## Program to find an element from the list using linear search method

## Function to linear search a country name in the given list
def search(key, countries):
    for item in countries:
        if key in item:
            print("{} exists in the list.".format(key))
            if key != item:
                print("Actual name in the list is: {}".format(item))
            return True
    print("{} doesn't exist in the list.".format(key))
    return False

## Initialising the list elements using a text file
with open("countries.txt", "r") as f:
    countries = f.read().splitlines()

## Asking the user to enter the country name
key = input("Enter the country name you want to find in the list: ")

## Call to function search
search(key, countries)
