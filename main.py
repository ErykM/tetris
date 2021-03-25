# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

from Move import LeftMove, RightMove, DownMove, RotateCounterClockwiseMove, RotateClockwiseMove


class Tetris:
    HEIGHT = 20
    WIDTH = 20
    MOVES = {
        'a': LeftMove,
        'd': RightMove,
        'w': RotateCounterClockwiseMove,
        's': RotateClockwiseMove
    }

    def __init__(self):
        self.board = [[0 for y in range(self.HEIGHT)] for x in range(self.WIDTH)]
        self.reset_board()

    def reset_board(self):
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                if i == self.HEIGHT - 1 or j == 0 or j == self.WIDTH - 1:
                    self.board[i][j] = '*'
                else:
                    self.board[i][j] = ' '

        return self.board

    def place_piece_on_board(self, piece):
        random_position = random.randint(1, self.WIDTH - len(piece.matrix) - 1)
        piece.x, piece.y = random_position, 0
        for i in range(len(piece.matrix)):
            print(i)
            for j in range(len(piece.matrix[i])):
                self.board[0 + i][random_position + j] = piece.matrix[i][j]

    def move(self, move, piece):
        if move not in self.MOVES.keys():
            return None

        self.MOVES.get(move)().execute(self.board, piece)
        self.print_board()
        DownMove().execute(self.board, piece)

    def print_board(self):
        print('---------------------------------------------------------')
        print('---------------------------------------------------------')

        for line in self.board:
            print(line)


class Piece:
    PIECES = {
        0: [['*', '*', '*', '*']],
        1: [['*', ' '], ['*', ' '], ['*', '*']],
        2: [[' ', '*'], [' ', '*'], ['*', '*']],
        3: [[' ', '*'], ['*', '*'], ['*', ' ']],
        4: [['*', '*'], ['*', '*']]
    }

    def __init__(self):
        # x,y are coordinates of top left cell
        self.x = 0
        self.y = 0
        # matrix is piece layout
        self.matrix = None

    def get_random_piece(self):
        choice = random.randint(0, 4)
        self.matrix = self.PIECES.get(choice)
        return self

    def is_movable(self):
        return True


class Game:
    ALLOWED_ACTIONS = ['a', 'd', 'w', 's']

    def __init__(self):
        self.tetris = Tetris()
        self.tetris.print_board()

    def start(self):
        curr_piece = self._board_new_piece()

        while not self._is_over():
            if not curr_piece.is_movable():
                curr_piece = self._board_new_piece()
            self.tetris.print_board()
            print('Choose your move')
            print('a - left\nd - right\nw - rotate counter clockwise\ns - rotate clockwise')
            move = input()

            if move in self.ALLOWED_ACTIONS:
                self.tetris.move(move, curr_piece)

    def _board_new_piece(self):
        piece = Piece().get_random_piece()
        self.tetris.place_piece_on_board(piece)
        return piece

    def _is_over(self):
        return False


class Runner:
    @staticmethod
    def run():
        g = Game()
        g.start()


if __name__ == '__main__':
    Runner.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
