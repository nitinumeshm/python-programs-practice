## Generate factorial of a number
## In this program, I'm using a recursive function

def factorial(x):
  if x == 1:
    return x
  else:
    return x * factorial(x-1)
  
num = int(input("Enter a number: "))
print("Factorial: ", factorial(num))
