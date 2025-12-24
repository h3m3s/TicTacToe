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


class DifficultBotPlayer(Player):
    """Trudny bot który używa algorytmu Minimax do analizy ruchów"""
    
    def __init__(self, symbol):
        super().__init__(symbol)
        self.opponent_symbol = "X" if symbol == "O" else "O"
    
    def get_move(self, board):
        print("Trudny Bot analizuje ruchy...")
        best_score = float('-inf')
        best_move = None
        for i in range(9):
            if board.cells[i] == " ":
                board.cells[i] = self.symbol
                score = self._minimax(board, 0, False, float('-inf'), float('inf'))
                board.cells[i] = " "
                
                if score > best_score:
                    best_score = score
                    best_move = i
        
        return best_move
    
    def _minimax(self, board, depth, is_maximizing, alpha, beta):
        if self._check_winner(board, self.symbol):
            return 10 - depth  
        
        if self._check_winner(board, self.opponent_symbol):
            return depth - 10
        
        if self._is_board_full(board):
            return 0  
        
        if is_maximizing:
            max_score = float('-inf')
            for i in range(9):
                if board.cells[i] == " ":
                    board.cells[i] = self.symbol
                    score = self._minimax(board, depth + 1, False, alpha, beta)
                    board.cells[i] = " "
                    max_score = max(score, max_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break  
            return max_score
        else:
            min_score = float('inf')
            for i in range(9):
                if board.cells[i] == " ":
                    board.cells[i] = self.opponent_symbol
                    score = self._minimax(board, depth + 1, True, alpha, beta)
                    board.cells[i] = " "
                    min_score = min(score, min_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break 
            return min_score
    
    def _check_winner(self, board, symbol):
        win_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        return any(board.cells[a] == board.cells[b] == board.cells[c] == symbol 
                   for a, b, c in win_positions)
    
    def _is_board_full(self, board):
        return " " not in board.cells


