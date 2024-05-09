## Game for guessing a number between 1 and 100

import random

secret_num = random.randint(1, 100)
attempts = 0

while True:
  guess = int(input("Guess a number between 1 and 100: "))
  attempts = attempts + 1
  if guess < secret_num:
    print("Too LOW!! Guess again!")
  elif guess > secret_num:
    print("Too HIGH!! Guess again!")
  else:
    if attempts == 1:
      print("BANG ON! You guessed it in first attempt!")
    else:
      print("You guessed the correct number in ", attempts, " attempts.")
    break
