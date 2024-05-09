#!/usr/bin/env python3

## Program to check if the given string is a palindrome or not
## In this program, we are going to change the string to lower case and then check if it's a palindrome or not

## Asking the user to enter a string of his/her choice
str = input("Enter a string: ")

reverse_str = str[::-1]

if reverse_str.lower() == str.lower():
  print("It's a PALINDROME!")
else:
  print("NOPE! It's NOT a PALINDROME")
