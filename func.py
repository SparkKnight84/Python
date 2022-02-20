import math
import random

# Calculates the factorial of the given number
def factorial(n: int):
  i = 1
  for m in range(1, n + 1):
    i *= m
  return i

# Returns True if the number given is even else returns False
def is_even(n: int):
  return n % 2 == 0

# Returns True if the number given is primt else returns False
def is_prime(n: int):
  if n == 1:
    return {"prime": False, "is_divisible_by": None}
  for m in range(2, int(n / 2) + 1):
    if n % m == 0:
      return {"prime": False, "is_divisible_by": m}
  return {"prime": True, "is_divisible_by": 1}

# Returns a list of allthe prime numbers before the given number
def arr_primes(n: int):
  arr = []
  for m in range(2, n + 1):
    if is_prime(m)["prime"]:
      arr.append(m)
  return arr

# Returns a random element from the list provided
def random_element_from_arr(arr: list):
  return arr[math.floor(random.randint(0, len(arr) - 1))]

# Returns a list ofgiven length with random elements fromthe given list
def random_arr_from_arr(arr: list, number_of_elements: int, duplicates_allowed: bool = False):
  new_arr = []
  while len(new_arr) < number_of_elements:
    rand = random_element_from_arr(arr)
    if not duplicates_allowed:
      if new_arr.count(rand) > 0:
        continue
      else:
        new_arr.append(rand)
    else:
      new_arr.append(rand)
  return new_arr

# Returns the distance between to coordinates
def distance_between_coords(x1: int, y1: int, x2: int, y2: int):
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Returns random hex color
def random_color():
  color_list = ['0','1','2','3','4','5','6','7','8','9',"a","b","c","d","e","f"]
  color = random_arr_from_arr(color_list, 6, True)
  code = "#"
  for i in color:
    code += i
  return code

# Returns the rgb of given hex color
def hex_to_rgb(hex_code):
  rgb_code = {"r": 0, "g": 0, "b": 0}
  
  return

# number = 100
# arr_of_nums = ["0","1","2","3","4","5","6","7","8","9"]
# print("Factorial of", number, ":", factorial(number))
# print(number, "is even:", is_even(number))
# print(number, "is prime:", is_prime(number)["prime"])
# print("Primes till", number, ":", arr_primes(number))
# print(random_arr_from_arr(arr_of_nums, 5))
# coords1 = {"x": 3, "y": 4}
# coords2 = {"x": 6, "y": 8}
# print(f"The distance between (" + str(coords1["x"]) + ", " + str(coords1["y"]) + ") and (" + str(coords2["x"]) + ", " + str(coords2["y"]) + ") is:", distance_between_coords(coords1["x"], coords1["y"], coords2["x"], coords2["y"]))
# print("Random color:", random_color())


def random_password(length, allow_symbols = True):
  alphabets_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  alphabets_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  symbols = ["!", "@", "#", "$", "&", "*"]
  numbers = ['1', '2', '3', '4','5', '6', '7', '8', '9', "0"]
  password = []
  password_string = ""
  while len(password) < length:
    if allow_symbols == True:
      password.append(random_element_from_arr(random_element_from_arr([alphabets_lower, alphabets_upper, symbols, numbers])))
    else:
      password.append(random_element_from_arr(random_element_from_arr([alphabets_lower, alphabets_upper, numbers])))
  for i in password:
    password_string += i
  return password_string

# print(random_password(12))

def password_bruteforce(original_password):
  password = random_password(len(original_password))
  n = 0
  while password != original_password:
    password = random_password(len(original_password))
    n+=1
    print(f"{n} | {original_password} | {password}")
  return password

# print(password_bruteforce(random_password(2)))

def number_guessing_game(input_func = input):
  number = random.randint(0, 1000)
  tries = 10
  while tries > 0:
    guess = int(input_func(f"Guess the number (tries left: {tries}) : "))
    if guess == number:
      print("Congratulations you won the guessing game!")
      return
    if guess > number:
      if guess - number > 500:
        print("Sorry! A bit too high")
      else:
        print("Sorry! A bit high")
    else:
      if number - guess > 500:
        print("Sorry! A bit too low")
      else:
        print("Sorry! A bit low")
    tries -= 1
  print(f"Sorry you lost the game! The correct number was {number}")

number_guessing_game()

# def number_guessing_game_ai():