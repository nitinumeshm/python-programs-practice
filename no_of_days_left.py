#!/usr/bin/env python3

## Program to find the number of days left from current day till the user mentioned day

from datetime import *

## Function to check if the given user date exists or not
def check_date_exists(year, month, day):
  try:
    date_obj = date(year, month, day)
    return True
  except ValueError:
    print("Date doesn't exist!")

## Function to check if the user given date is in the future or not
def check_if_future_date(year, month, day):
  given_date = date(year, month, day)
  if given_date > date.today():
    return True
  else:
    print("Date is not in the future!")

day_name = input("Name the special day that is coming for you in the future: ")
year = int(input("Enter Year: "))
month = int(input("Enter Month: "))
day = int(input("Enter Day: "))

if check_date_exists(year, month, day) == True and check_if_future_date(year, month, day) == True:
  d_day = date(year, month, day)
  days_left = abs(d_day - date.today())
  print("Number of Days left to {}: {}".format(day_name, days_left))

  
