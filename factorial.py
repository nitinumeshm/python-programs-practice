## Calculate the factorial of a given number

def fact(x):
  if x == 0:
    print("Factorial of the given number: ", 1)
  else:
    result = x
    while x!= 1:
      result = result * (x - 1)
      x = x - 1
    print("Factorial of the given number: ", result)

num = int(input("Enter any whole number: "))

if num < 0:
  print("Invalid. Given number is not a whole number!!")
else:
  fact(num)
