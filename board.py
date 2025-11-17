import os, sys
def clear():
    print("\n" * 50)
class Board:

    def __init__(self):
        self.reset()

    def reset(self):
        self.cells = [" " for _ in range(9)]

    def display(self):
        clear()
        print()
        print(f" {self._cell(0)} | {self._cell(1)} | {self._cell(2)}")
        print("---+---+---")
        print(f" {self._cell(3)} | {self._cell(4)} | {self._cell(5)}")
        print("---+---+---")
        print(f" {self._cell(6)} | {self._cell(7)} | {self._cell(8)}")
        print()

    def _cell(self, i):
        return self.cells[i] if self.cells[i] != " " else str(i+1)

    def make_move(self, index, symbol):
        if self.cells[index] == " ":
            self.cells[index] = symbol
            return True
        return False

    def is_full(self):
        return " " not in self.cells

    def check_winner(self, symbol):
        win_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 1, 2), (2, 4, 6)
        ]
        return any(self.cells[a] == self.cells[b] == self.cells[c] == symbol for a, b, c in win_positions)

