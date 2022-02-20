# TIC-TAC-TOE

slots = {
  1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "
}

def print_formatted(info):
  board = f"{info[1]} | {info[2]} | {info[3]}\n{info[4]} | {info[5]} | {info[6]}\n{info[7]} | {info[8]} | {info[9]}"
  print(board)

print_formatted(slots)

def is_movable(move):
  if slots[move] != " ":
    return False
  return True

def p1_input():
  move = int(input("P1 - Input your move: "))
  movable = False
  while not movable:
    movable = is_movable(move)
    if not movable:
      print(f"Slot {move} is already occupied by {slots[move]}")
      move = int(input("P1 - Input your move: "))
  slots[move] = "X"

def p2_input():
  move = int(input("P2 - Input your move: "))
  movable = False
  while not movable:
    movable = is_movable(move)
    if not movable:
      print(f"Slot {move} is already occupied by {slots[move]}")
      move = int(input("P2 - Input your move: "))
  slots[move] = "O"

def check_win():
  conditions = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
  for condition in conditions:
    if slots[condition[0]] == slots[condition[1]] and slots[condition[1]] == slots[condition[2]] and slots[condition[0]] != " ":
      return True
  return False

def start():
  turn = 0
  while turn <= 8:
    if turn % 2 == 0:
      p1_input()
    else:
      p2_input()
    print_formatted(slots)
    if check_win():
      print(f"Player {(turn % 2) + 1} won the game!")
      return
    turn += 1
  print("The game is a draw!")

def main():
  start()

if __name__ == "__main__":
  main()