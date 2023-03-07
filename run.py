def playing_board():
    """
    Creates the vitual playing board
    """
    print("   A  B  C  D  E  F")
    print("+++++++++++++++++++++")
    board = [["| " for num in range(6)] for num in range(6)]
    row_num = 1
    for row in board:
        print(row_num, " ".join(row))
        row_num += 1
    print("+++++++++++++++++++++")


playing_board()
