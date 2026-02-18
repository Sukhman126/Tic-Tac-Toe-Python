board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    # Rows
    if (board[0] == board[1] == board[2] == player or
        board[3] == board[4] == board[5] == player or
        board[6] == board[7] == board[8] == player):
        return True
    
    # Columns
    if (board[0] == board[3] == board[6] == player or
        board[1] == board[4] == board[7] == player or
        board[2] == board[5] == board[8] == player):
        return True
    
    # Diagonals
    if (board[0] == board[4] == board[8] == player or
        board[2] == board[4] == board[6] == player):
        return True
    
    return False

def is_draw():
    return " " not in board

# Main Game
current_player = "X"

while True:
    print_board()
    position = int(input("Player " + current_player + ", choose position (1-9): ")) - 1

    if board[position] == " ":
        board[position] = current_player

        if check_winner(current_player):
            print_board()
            print("Player", current_player, "wins! 🎉")
            break

        if is_draw():
            print_board()
            print("It's a draw!")
            break

        # Switch player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    else:
        print("Position already taken! Try again.")
