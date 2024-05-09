## Print the arithmetic function of previous and current numbers till the range 10

current_num = int(input("Enter the starting number: "))
prev_num = current_num - 1

for current_num in range(current_num, current_num + 10):
  sum = prev_num + current_num
  prod = prev_num * current_num
  print("{} + {} = {}\t\t\t\t\t{} * {} = {}".format(prev_num, current_num, sum, prev_num, current_num, prod))
  prev_num = current_num
