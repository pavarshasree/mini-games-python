board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8],   # columns
        [0,4,8], [2,4,6]             # diagonals
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_draw():
    return "-" not in board

current_player = "X"

while True:
    print_board()
    
    try:
        move = int(input(f"Player {current_player}, choose position (1-9): ")) - 1
        
        if move < 0 or move > 8:
            print("Invalid position! Choose 1-9.")
            continue
        
        if board[move] == "-":
            board[move] = current_player
        else:
            print("Position already taken! Try again.")
            continue
            
    except ValueError:
        print("Please enter a number!")
        continue
    
    if check_winner(current_player):
        print_board()
        print(f"🎉 Player {current_player} wins!")
        break
    
    if is_draw():
        print_board()
        print("It's a Draw!")
        break
    
    current_player = "O" if current_player == "X" else "X"