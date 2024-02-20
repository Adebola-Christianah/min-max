import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Representing the Tic-Tac-Toe board as a list

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_spots(self):
        return ' ' in self.board

    def winning(self, player):
        # Check rows, columns, and diagonals for winning conditions
        win_state = [
            [self.board[0], self.board[1], self.board[2]],
            [self.board[3], self.board[4], self.board[5]],
            [self.board[6], self.board[7], self.board[8]],
            [self.board[0], self.board[3], self.board[6]],
            [self.board[1], self.board[4], self.board[7]],
            [self.board[2], self.board[5], self.board[8]],
            [self.board[0], self.board[4], self.board[8]],
            [self.board[2], self.board[4], self.board[6]],
        ]
        return [player, player, player] in win_state

    def make_move(self, position, player):
        self.board[position] = player

    def undo_move(self, position):
        self.board[position] = ' '

    def minimax(self, depth, maximizing_player):
        if self.winning('O'):
            return {'score': 1}
        elif self.winning('X'):
            return {'score': -1}
        elif not self.empty_spots():
            return {'score': 0}

        if maximizing_player:
            best = {'move': -1, 'score': -math.inf}
            for move in self.available_moves():
                self.make_move(move, 'O')
                result = self.minimax(depth+1, False)
                self.undo_move(move)
                result['move'] = move

                if result['score'] > best['score']:
                    best = result
        else:
            best = {'move': -1, 'score': math.inf}
            for move in self.available_moves():
                self.make_move(move, 'X')
                result = self.minimax(depth+1, True)
                self.undo_move(move)
                result['move'] = move

                if result['score'] < best['score']:
                    best = result

        return best

    def find_best_move(self):
        return self.minimax(0, True)['move']


# Example usage:
if __name__ == "__main__":
    game = TicTacToe()
    game.print_board()
    while game.empty_spots() and not game.winning('O') and not game.winning('X'):
        player_move = int(input("Enter your move (0-8): "))
        game.make_move(player_move, 'X')
        game.print_board()

        if game.winning('X'):
            print("You win!")
            break

        if not game.empty_spots():
            print("It's a tie!")
            break

        print("Computer's move...")
        computer_move = game.find_best_move()
        game.make_move(computer_move, 'O')
        game.print_board()

        if game.winning('O'):
            print("Computer wins!")
            break

        if not game.empty_spots():
            print("It's a tie!")
            break
