# Tic Tac Toe

# Create the board
board = [" " for _ in range(9)]

# Display the board
def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
    separator = "-------------"
    print()
    print(row1)
    print(separator)
    print(row2)
    print(separator)
    print(row3)
    print()

# Check for a win
def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True

    return False

# Play the game
def play_game():
    print("Welcome to Tic Tac Toe!")
    print_board()
    player = "X"

    while True:
        position = int(input("Enter a position (1-9): ")) - 1

        if board[position] == " ":
            board[position] = player
            print_board()

            if check_win(player):
                print("Player {} wins! Congratulations!".format(player))
                break

            if " " not in board:
                print("It's a tie!")
                break

            player = "O" if player == "X" else "X"
        else:
            print("That position is already filled. Try again.")

# Start the game
play_game()