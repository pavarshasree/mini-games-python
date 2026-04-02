ROWS = 6
COLS = 7

board = [[" " for i in range(COLS)] for j in range(ROWS)]

def print_board():
    for row in board:
        print("|".join(row))
        print("-"*13)

def drop_piece(col, piece):
    for r in range(ROWS-1, -1, -1):
        if board[r][col] == " ":
            board[r][col] = piece
            return True
    return False

def check_win(piece):

    # Horizontal
    for r in range(ROWS):
        for c in range(COLS-3):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Vertical
    for c in range(COLS):
        for r in range(ROWS-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Diagonal \
    for r in range(ROWS-3):
        for c in range(COLS-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Diagonal /
    for r in range(3, ROWS):
        for c in range(COLS-3):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

    return False


player = 1
game_over = False

print("CONNECT FOUR GAME")

while not game_over:

    print_board()

    col = int(input(f"Player {player}, choose column (0-6): "))

    piece = "X" if player == 1 else "O"

    if drop_piece(col, piece):

        if check_win(piece):
            print_board()
            print(f"Player {player} wins!")
            game_over = True

        player = 2 if player == 1 else 1

    else:
        print("Column full! Try another column.")