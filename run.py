from random import randint

PLAYER_BOARD = [[" " for num in range(6)] for num in range(6)]
GUESS_BOARD = [[" " for num in range(6)] for num in range(6)]
COMP_BOARD = [[" " for num in range(6)] for num in range(6)]

def player_name():
    """
    Get players name to display over playing board
    """
    while True:
        name = input("- My name is ")

        if valid_name(name):
            print(f"\nWelcome {name.capitalize()}!")
            break

def valid_name(value):
    """
    Check that value is only letters
    """
    try:
        if value.isalpha() != True:
            raise ValueError(
                "\nName can only consist of letters."
            )
    except ValueError as e:
        print(f" {e} Please try again.\n")
        return False

    return True


def playing_board(board):
    """
    Create the vitual playing board
    """
    print("  A  B  C  D  E  F")
    print("++++++++++++++++++++")
    row_num = 1
    for row in board:
        print(row_num, " |".join(row))
        row_num += 1
    print("++++++++++++++++++++")


def gen_ships(board):
    """
    Generate random placement of ships
    """
    for ship in range(5):
        ship_row = randint(0, 5)
        ship_column = randint(0, 5)
        while board[ship_row][ship_column] == "o":
            ship_row = randint(0, 5)
            ship_column = randint(0, 5)
        board[ship_row][ship_column] = "o"


def player_guess():
    """
    Get guess input from player
    """
    while True:
        row = input("\nEnter a guess for row, between 1-6: ")
        column = input("Enter a guess for column, between A-F: ").upper()

        if valid_guess(row, column):
            break


def valid_guess(value1, value2):
    """
    Check that each value only consists of one character.
    That value1 consists of a number between 1 and 6,
    and that value2 consists of a letter between A and F.
    """
    try:
        if len(value1) | len(value2) !=1:
            raise ValueError(
                "\nEach guess can only consist of one character."
            )
        elif value1 not in "123456":
            raise ValueError(
                "\nRow guess can only be a number between 1-6."
            )
        elif value2 not in "ABCDEF":
            raise ValueError(
                "\nColumn guess can only be a letter between A-F."
            )
    except ValueError as e:
        print(f" {e} Please make another guess.")
        return False
    
    return True


def main():
    print("\nDo you want to play battleships with me?\n")
    print("Enter your name if you want to.")
    player_name()
    gen_ships(PLAYER_BOARD)
    gen_ships(COMP_BOARD)
    print(f"\nThis is your board")
    playing_board(PLAYER_BOARD)
    print("\nThis is the computers board")
    print("Think of it as your guessing board")
    playing_board(GUESS_BOARD)
    player_guess()

main()

