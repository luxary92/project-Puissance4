ROWS = 6
COLS = 7
"""Crée une grille vide de taille ROWS x COLS"""
def create_board():
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    print("\n  0   1   2   3   4   5   6")
    print("+" + "---+"*COLS)
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+" + "---+"*COLS)
 """Vérifie si un coup est valide (colonne non pleine)"""
def is_valid_move(board, col):
    return board[0][col] == " "

def get_next_open_row(board, col):
    for r in range(ROWS-1, -1, -1):
        if board[r][col] == " ":
            return r
    return None

def drop_piece(board, row, col, piece):
    board[row][col] = piece

"""Vérifie si le joueur a gagné (4 jetons alignés)"""
def winning_move(board, piece):
    #A l'horizontal
    for r in range(ROWS):
        for c in range(COLS-3):
            if all(board[r][c+i] == piece for i in range(4)):
                return True
    # A la vertical
    for c in range(COLS):
        for r in range(ROWS-3):
            if all(board[r+i][c] == piece for i in range(4)):
                return True
    #En  diagonale vers la droite  
    for r in range(3, ROWS):
        for c in range(COLS-3):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True
    # En diagonale vers la gauche 
    for r in range(ROWS-3):
        for c in range(COLS-3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True
    return False


def full_board(board):
    return all(board[0][c] != " " for c in range(COLS))

def main():
    board = create_board()
    game_over = False
    turn = 0
    pieces = ["X", "O"]

    print_board(board)
    
    while not game_over:
        col = input(f"Joueur {turn+1} ({pieces[turn]}), entre la colonne (0-{COLS-1}): ")
        if not col.isdigit() or int(col) not in range(COLS):
            print("Colonne invalide, réessayez.")
            continue
        col = int(col)

        if is_valid_move(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, pieces[turn])
            print_board(board)

            if winning_move(board, pieces[turn]):
                print(f"GG ! Joueur {turn+1} ({pieces[turn]}) a win !")
                game_over = True
            elif full_board(board):
                print("Egalité")
                game_over = True
            else:
                turn = (turn + 1) % 2
        else:
            print("Colonne replie, réessayez")

if __name__ == "__main__":
    main()
