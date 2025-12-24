from board import Board
from player import HumanPlayer, BotPlayer, DifficultBotPlayer

class Game:
    def __init__(self, vs_bot=False, difficult=False):
        self.board = Board()
        self.player_x = HumanPlayer("X")
        if vs_bot:
            self.player_o = DifficultBotPlayer("O") if difficult else BotPlayer("O")
        else:
            self.player_o = HumanPlayer("O")

    def play(self):
        current = self.player_x
        self.board.display()

        while True:
            move = current.get_move(self.board)
            self.board.make_move(move, current.symbol)
            self.board.display()

            if self.board.check_winner(current.symbol):
                print(f"Wygrywa {current.symbol}!")
                break

            if self.board.is_full():
                print("Remis!")
                break

            current = self.player_o if current == self.player_x else self.player_x


