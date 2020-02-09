import random

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def print_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

def random_number():
    return random.randint(0,9)

def player_one():
    move = input("Player 1: Enter move (1 - 9)")
    if validate_move(int(move)):
        board[int(move) - 1] = "0"
        print_board(board)
    else:
        print("Move is invalid")
        player_one()

def player_two():
    move = input("Player 2: Enter move (1 - 9)")
    if validate_move(int(move)):
        board[int(move) - 1] = "X"
        print_board(board)
    else:
        print("Move is invalid")
        player_two()

def auto_player_two():
    move = random_number()
    while(validate_move(int(move)) == False):
        move = random_number()
    board[int(move) - 1] = "X"
    print("player 2 move:")
    print_board(board)

def validate_move(move):
    if move <= 9 and move > 0:
        if board[move - 1] != " ":
            return False
        else:
            return True
    else:
        return False

def play_game():
    loop = 0
    print_board(board)
    while loop < 9:
        player_one()
        loop += 1
        player_two()
        loop += 1

play_game()