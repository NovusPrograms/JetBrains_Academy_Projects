def make_matrix(game_status):
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            matrix[i][j] = game_status[j + 3 * i]
    return matrix


def is_player_win(matrix, player):
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == player:
        return True
    if matrix[0][2] == matrix[1][1] == matrix[2][0] == player:
        return True
    for n in range(3):
        if matrix[n] == [player, player, player] \
                or matrix[0][n] == matrix[1][n] == matrix[2][n] == player:
            return True
    return False


def is_all_filled(matrix):
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == " ":
                return False
    return True


def is_game_run(matrix, player1, player2):
    if not is_player_win(matrix, player1) and not is_player_win(matrix, player2) and not is_all_filled(matrix):
        return True
    return False


def is_cell_free(a, b, matrix):
    if matrix[abs(b - 4) - 1][a - 1] == " ":
        return True
    return False


def print_table(matrix):
    structure = {
        "floor": "---------",
        "row0": "| " + " ".join(matrix[0]) + " |",
        "row1": "| " + " ".join(matrix[1]) + " |",
        "row2": "| " + " ".join(matrix[2]) + " |"}

    print(structure["floor"])
    print(structure["row0"])
    print(structure["row1"])
    print(structure["row2"])
    print(structure["floor"])


def make_move(matrix, player):
    while True:
        try:
            next_move = list(map(int, input("Enter the coordinates: > ").split()))

            if next_move[0] in {1, 2, 3} and next_move[1] in {1, 2, 3}:
                if is_cell_free(next_move[0], next_move[1], matrix_variable):
                    matrix[abs(next_move[1] - 4) - 1][next_move[0] - 1] = player
                    break
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")

        except ValueError:
            print("You should enter numbers!")
    return matrix


def end_game_statement(matrix, player1, player2):
    if is_player_win(matrix_variable, player1):
        print_table(matrix)
        print(f"{mark1} wins")
    elif is_player_win(matrix_variable, player2):
        print_table(matrix)
        print(f"{mark2} wins")
    else:
        print_table(matrix)
        print("Draw")
    
    
def play(matrix, player1, player2):
    while is_game_run(matrix, player1, player2):
        print_table(matrix)
        make_move(matrix, player1)
        if is_game_run(matrix, player1, player2):
            print_table(matrix)
            make_move(matrix, player2)
    
    
mark1 = "X"
mark2 = "O"
input_status = "         "
matrix_variable = make_matrix(input_status)


play(matrix_variable, mark1, mark2)
end_game_statement(matrix_variable, mark1, mark2)
