## Print and count the number of factors for a given number

def factor(x):
  if x == 0:
    print("Number of factors for the given number: ", 0)
  else:
    i = 1
    counter = 0
    while i <= x:
      if x % i == 0:
        print(i)
        counter += 1
      i += 1  
    print("Number of factors for the given number: ", counter)
    
num = int(input("Enter a whole number: "))
factor(num)
