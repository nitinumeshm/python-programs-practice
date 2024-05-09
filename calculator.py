## Calculator to perform basic arithmetic functions

def addition(x, y):
  return (x + y)

def subtraction(x, y):
  return (x - y)

def multiplication(x, y):
  return (x * y)

def division(x, y):
  if y != 0:
    return (x / y)
  else:
    print("Cannot divide by 0!!")

print("Select operation")
print("1. Addition")
print("2: Subtraction")
print("3. Multiplication")
print("4: Division")

choice = float(input("Enter your choice (1/2/3/4): "))
if choice > 0 and choice < 5:
  num1 = float(input("First Number: "))
  num2 = float(input("Second Number: "))
  if choice == 1:
    print(num1, "+", num2, "=", addition(num1, num2))
  elif choice == 2:
    print(num1, "-", num2, "=", subtraction(num1, num2))
  elif choice == 3:
    print(num1, "*", num2, "=", multiplication(num1, num2))
  elif choice == 4:
    print(num1, "/", num2, "=", division(num1, num2))
else:
  print("Invalid Choice!!")
