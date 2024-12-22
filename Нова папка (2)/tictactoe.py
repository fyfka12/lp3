class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"


    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            return True
        return False

    def check_win(self):
        # Перевірка рядків
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return True

        # Перевірка стовпців
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return True

        # Перевірка діагоналей
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True

        return False

    def check_draw(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def start_game(self):
        while True:
            self.print_board()
            row = int(input(f"Гравець {self.current_player}, введіть номер рядка (0-2): "))
            col = int(input(f"Гравець {self.current_player}, введіть номер стовпця (0-2): "))
            if self.make_move(row, col):
                if self.check_win():
                    self.print_board()
                    print(f"Гравець {self.current_player} переміг!")
                    break
                elif self.check_draw():
                    self.print_board()
                    print("Нічия!")
                    break
                else:
                    self.current_player = "X" if self.current_player == "O" else "O"
            else:
                print("Ця клітинка вже зайнята. Спробуйте іншу.")
