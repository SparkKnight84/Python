def calc():
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))
  operator = input("Enter the operator (+, -, *, /) :")

  if(operator == "+"):
    print(num1 + num2)
  elif(operator == "-"):
    print(num1 - num2)
  elif(operator == "*"):
    print(num1 * num2)
  elif(operator == "/"):
    print(num1 / num2)
  else:
    print("Please choose a valid operator next time (+, -, *, /)")

# calc()

def factorial(num):
  if num == 0 or num == 1:
    return 1
  i = 1
  result = 1
  while i <= num:
    result *= i
    i += 1
  return result

# print(factorial(4))

def advcalc(str):
  arr = str.split(" ")
  for i in arr:
    type_of_i = int(i)
    print(type_of_i)
  print(arr)

# advcalc("2 + 2")

import random

i = 0
one_count = 0
two_count = 0
my_binary = int

while i < 1000 * 1000 * 1 * 1:
  m = random.randint(0, 1)
  if m == 1:
    one_count += 1
  else:
    two_count += 1
  # print(i, ": ", m)

  i += 1

print(one_count)
print(two_count)