board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def print_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

def player_one():
    move = input("Player 1: Enter move (1 - 9)")
    board[int(move) - 1] = "0"
    print_board(board)

def player_two():
    move = input("Player 2: Enter move (1 - 9)")
    board[int(move) - 1] = "X"
    print_board(board)

def play_game():
    loop = 0
    print_board(board)
    while loop < 9:
        player_one()
        loop += 1
        player_two()
        loop += 1

play_game()