import random

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        raise NotImplementedError


class HumanPlayer(Player):
    def get_move(self, board):
        while True:
            try:
                move = int(input(f"Gracz {self.symbol}, podaj ruch (1-9): ")) - 1
                if move in range(9) and board.cells[move] == " ":
                    return move
            except ValueError:
                pass
            print("Nieprawidłowy ruch, spróbuj ponownie.")


class BotPlayer(Player):
    def get_move(self, board):
        print("Bot myśli...")
        empty = [i for i, v in enumerate(board.cells) if v == " "]
        return random.choice(empty)


