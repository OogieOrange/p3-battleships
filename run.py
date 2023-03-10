from random import randint

PLAYER_BOARD = [[" " for num in range(7)] for num in range(6)]
GUESS_BOARD = [[" " for num in range(7)] for num in range(6)]
COMP_BOARD = [[" " for num in range(6)] for num in range(6)]

column_number = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}

r_guess = 0
c_guess = 0

blue = "\033[38;5;14m"
green = "\033[38;5;29m"
red = "\033[31;5;29m"
no_color = "\033[0;0;0m"


def player_name():
    """
    Get players name to display over playing board
    """
    while True:
        name = input("- My name is ")

        if valid_name(name):
            print(f"\nWelcome {green}{name.capitalize()}!{no_color}")
            break


def valid_name(value):
    """
    Check that value is only letters
    """
    try:
        if value.isalpha() is not True:
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
    print("  A  B  C  D  E  F   ")
    print("++++++++++++++++++++ ")
    row_num = 1
    for row in board:
        print(row_num, "| ".join(row))
        row_num += 1
    print(f"++++++++++++++++++++ {no_color}")


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
        global r_guess, c_guess
        row = input("\nEnter a guess for row, between 1-6: ")
        column = input("Enter a guess for column, between A-F: ").upper()

        if valid_guess(row, column):
            break

    r_guess = int(row) - 1
    c_guess = column_number[column]

    return r_guess, c_guess


def valid_guess(value1, value2):
    """
    Check that each value only consists of one character.
    That value1 consists of a number between 1 and 6,
    and that value2 consists of a letter between A and F.
    """
    try:
        if len(value1) != 1 or len(value2) != 1:
            raise ValueError(
                "\nEach guess can only consist of one character."
            )
        elif value1 == "" or value2 == "":
            raise ValueError(
                "\nYou cannot make an empty guess."
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


def player_hit(board, board2):
    """
    Check if player hit comp ship
    """
    while board[r_guess][c_guess] == "-" or board[r_guess][c_guess] == "x":
        print("\nYou've already guessed those cordinates. Guess again.")
        player_guess()
    if board[r_guess][c_guess] == "o":
        board[r_guess][c_guess] = "x"
        board2[r_guess][c_guess] = "x"
        print("\n- Oh no! You hit my ship!")
    else:
        board[r_guess][c_guess] = "-"
        board2[r_guess][c_guess] = "-"
        print("\n- Haha! You missed my ships.")


def comp_guess(board):
    """
    Genereate computer guess and check for hit,
    otherwise show miss on player board
    """
    for guess in range(1):
        row = randint(0, 5)
        column = randint(0, 5)
        while board[row][column] == "-" or board[row][column] == "x":
            row = randint(0, 5)
            column = randint(0, 5)
        if board[row][column] == "o":
            board[row][column] = "x"
            print("- I hit your ship!")
        else:
            board[row][column] = "-"
            print("- I missed...")


def ships_hit(board):
    """
    Check how many hits a board hasS
    """
    hit_ships = 0
    for row in board:
        for column in row:
            if column == "x":
                hit_ships += 1
    return hit_ships


def reset_board(board):
    """
    Reset board to be empty
    """
    r = randint(0, 5)
    c = randint(0, 5)
    while True:
        if board[r][c] == "-" or board[r][c] == "x" or board[r][c] == "o":
            board[r][c] = " "
        elif board[r][c] == " ":
            symbols = check_board(board)
            if symbols > 0:
                r = randint(0, 5)
                c = randint(0, 5)
            else:
                break


def check_board(board):
    """
    Check board for symbols
    """
    symbols = 0
    for row in board:
        for column in row:
            if column == "-" or column == "x" or column == "o":
                symbols += 1
    return symbols


def continue_game():
    """
    Check if player wants to end or play again
    """
    while True:
        answer = input("Enter answer: ").lower()

        if answer == "y":
            break
        elif answer == "n":
            break
        else:
            print("\nThe answer must be either 'y' or 'n'.")

    if answer == "y":
        print("\nHere we go again!")
        main()
    elif answer == "n":
        print("\nIt was nice playing with you.")
        print("Have a nice day! :)")


def intro_txt():
    """
    Startes game through asking for players name,
    and prints rules
    """
    print("\nDo you want to play battleships with me?\n")
    print("Enter your name,")
    player_name()
    print("\n- Guess what cordinates hides my ships, and I will guess yours!")
    print("- If a ship is hit, it will show an 'x' to mark the spot.")
    print("- If it's a miss, it will instead show a '-' to indicate this.")
    print("- The 'o' on your board are your ships.")
    print("- I can't see them, like you can't see mine.")
    print("- Frist to 5 sunken oponent ships wins!")


def main():
    """
    Runs game
    """
    gen_ships(PLAYER_BOARD)
    gen_ships(COMP_BOARD)
    while True:
        print(f"\n{green}This is your board{no_color},\n{blue}")
        playing_board(PLAYER_BOARD)
        print("\nThis is your guessing board.")
        print(f"{red}My board is behind this board{no_color},\n{blue}")
        playing_board(GUESS_BOARD)
        print("\nMake a guess!")
        player_guess()
        player_hit(COMP_BOARD, GUESS_BOARD)
        player_ship_hit = ships_hit(COMP_BOARD)
        print(f"{green}Your score is{no_color}: {player_ship_hit}\n")
        comp_guess(PLAYER_BOARD)
        comp_ship_hit = ships_hit(PLAYER_BOARD)
        print(f"{red}My score is{no_color}: {comp_ship_hit}")
        if player_ship_hit == 5 and comp_ship_hit == 5:
            print("\nIt's a Draw!")
            reset_board(PLAYER_BOARD)
            reset_board(GUESS_BOARD)
            reset_board(COMP_BOARD)
            break
        elif player_ship_hit == 5:
            print(f"\n{green}You won{no_color}!")
            reset_board(PLAYER_BOARD)
            reset_board(GUESS_BOARD)
            reset_board(COMP_BOARD)
            break
        elif comp_ship_hit == 5:
            print(f"\n{red}I won{no_color}!")
            reset_board(PLAYER_BOARD)
            reset_board(GUESS_BOARD)
            reset_board(COMP_BOARD)
            break
    print("\nWould you like to play again?")
    print(f"If yes then answer 'y', else 'n' for no.\n")
    continue_game()


intro_txt()
main()
