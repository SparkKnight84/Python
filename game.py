# TIC-TAC-TOE

slots = {
  1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "
}

def print_formatted(info):
  board = f"""
  {info[1]} | {info[2]} | {info[3]}
  {info[4]} | {info[5]} | {info[6]}
  {info[7]} | {info[8]} | {info[9]}"""
  print(board)

print_formatted(slots)

def is_movable(move):
  if slots[move] != "":
    return False
  return True

def not_movable(move):
  if not is_movable(move):
    print(f"Slot {move} is already occupied by {slots[move]}")

def p1_input():
  move = int(input("P1 - Input your move: "))
  slots[move] = "X"

def p2_input():
  move = int(input("P2 - Input your move: "))
  slots[move] = "O"

p1_input()

print_formatted(slots)

p2_input()

print_formatted(slots)

p1_input()

print_formatted(slots)

p2_input()

print_formatted(slots)

p1_input()

print_formatted(slots)

p2_input()

print_formatted(slots)

p1_input()

print_formatted(slots)

p2_input()

print_formatted(slots)

p1_input()

print_formatted(slots)