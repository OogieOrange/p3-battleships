from random import randint

PLAYER_BOARD = [[" " for num in range(6)] for num in range(6)]
GUESS_BOARD = [[" " for num in range(6)] for num in range(6)]

def player_name():
    """
    Get players name to display over playing board
    """
    while True:
        name = input("What is your name?  ")

        if valid_name(name):
            print(f"\nWelcome {name.capitalize()}!")
            break
    return name

def valid_name(value):
    """
    Check that name is only letters
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
    Creates the vitual playing board
    """
    print("\n  A  B  C  D  E  F")
    print("++++++++++++++++++++")
    row_num = 1
    for row in board:
        print(row_num, " |".join(row))
        row_num += 1
    print("++++++++++++++++++++")


def gen_ships(board):
    """
    Generates ransom placement of ships
    """
    for ship in range(5):
        ship_row = randint(0, 5)
        ship_column = randint(0, 5)
        while board[ship_row][ship_column] == "o":
            ship_row = randint(0, 5)
            ship_column = randint(0, 5)
        board[ship_row][ship_column] = "o"


def main():
    print("\nDo you want to play battleships with me?\n")
    print("Enter your name if you ant to.")
    player_name()
    gen_ships(PLAYER_BOARD)
    playing_board(PLAYER_BOARD)
    playing_board(GUESS_BOARD)

main()

