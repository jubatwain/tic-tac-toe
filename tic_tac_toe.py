# A simple tic tac toe game in python

# Define the board as a list of 9 empty strings
board = [" "] * 9

# Define the symbols for the players
player1 = "X"
player2 = "O"

# Define a function to display the board
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

# Define a function to check if the board is full
def is_full():
    return " " not in board

# Define a function to check if a player has won
def is_winner(symbol):
    # Check the rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == symbol:
            return True
    # Check the columns
    for i in range(0, 3):
        if board[i] == board[i+3] == board[i+6] == symbol:
            return True
    # Check the diagonals
    if board[0] == board[4] == board[8] == symbol:
        return True
    if board[2] == board[4] == board[6] == symbol:
        return True
    # No winner
    return False

# Define a function to get a valid move from a player
def get_move(symbol):
    while True:
        # Prompt the player for a position (1-9)
        position = input(f"Player {symbol}, enter a position (1-9): ")
        # Validate the input
        if position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Invalid input. Please enter a number between 1 and 9.")
        else:
            # Convert the position to an index (0-8)
            index = int(position) - 1
            # Check if the position is available
            if board[index] != " ":
                print("That position is already taken. Please choose another one.")
            else:
                # Return the index
                return index

# Define a function to play the game
def play_game():
    # Display the initial board
    display_board()
    # Loop until the game is over
    while True:
        # Get a move from player 1
        index = get_move(player1)
        # Place the symbol on the board
        board[index] = player1
        # Display the updated board
        display_board()
        # Check if player 1 has won
        if is_winner(player1):
            print(f"Player {player1} wins!")
            break
        # Check if the board is full
        if is_full():
            print("It's a tie!")
            break
        # Get a move from player 2
        index = get_move(player2)
        # Place the symbol on the board
        board[index] = player2
        # Display the updated board
        display_board()
        # Check if player 2 has won
        if is_winner(player2):
            print(f"Player {player2} wins!")
            break
        # Check if the board is full
        if is_full():
            print("It's a tie!")
            break

# Start the game
play_game()
