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

print_board(board)
player_one()