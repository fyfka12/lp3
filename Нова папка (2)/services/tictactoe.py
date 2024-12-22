def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)


def make_move(row, col, current_player, board):
    if board[row][col] == " ":
        board[row][col] = current_player
        return True
    return False


def check_win(board):
    # Перевірка рядків
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Перевірка стовпців
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Перевірка діагоналей
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True
