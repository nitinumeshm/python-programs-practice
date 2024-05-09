## Create multiplication table upto 10 for a given number

def mult_table(x):
  if x == 0:
    print("No need for a table, as anything multiplied by 0 is 0!")
  else:
    for multiplier in range(1, 10+1):
      result = x * multiplier
      print(x, " * ", multiplier, " = ", result)

num = int(input("Enter a number: "))
mult_table(num)
