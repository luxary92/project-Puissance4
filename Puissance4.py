ROWS = 6
COLS = 7

def create_board():
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    print("\n  0   1   2   3   4   5   6")
    print("+" + "---+"*COLS)
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+" + "---+"*COLS)
