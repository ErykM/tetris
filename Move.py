class Move:
    ADDED = []

    def execute(self, board, piece):
        raise NotImplemented('Move execute method is not implemented')


def print_board(board):
    print('---------------------------------------------------------')
    print('---------------------------------------------------------')

    for line in board:
        print(line)


class DownMove(Move):
    ADDED = []

    def execute(self, board, piece):
        self.ADDED.clear()
        matrix = piece.matrix
        x, y = piece.x, piece.y

        for i_y_axis in range(len(matrix)):
            for j_x_axis in range(len(matrix[i_y_axis])):
                if (y + i_y_axis, x + j_x_axis) not in self.ADDED:
                    board[y + i_y_axis][x + j_x_axis] = ' '

                temp_y = y + i_y_axis + 1
                temp_x = x + j_x_axis
                self.ADDED.append((temp_y, temp_x))
                board[temp_y][temp_x] = matrix[i_y_axis][j_x_axis]

        piece.y += 1


class LeftMove(Move):
    ADDED = []

    def execute(self, board, piece):
        self.ADDED.clear()
        matrix = piece.matrix
        x, y = piece.x, piece.y

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (y + i, x + j) not in self.ADDED:
                    board[y + i][x + j] = ' '

                temp_y = y + i
                temp_x = x + j - 1
                self.ADDED.append((temp_y, temp_x))

                board[y + i][x + j - 1] = matrix[i][j]

        piece.x -= 1


class RightMove(Move):
    ADDED = []

    def execute(self, board, piece):
        self.ADDED.clear()
        matrix = piece.matrix
        x, y = piece.x, piece.y

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (y + j, x + i) not in self.ADDED:
                    board[y + j][x + i] = ' '

                temp_y = y + j
                temp_x = x + i + 1
                self.ADDED.append((temp_y, temp_x))

                board[y + j][x + i + 1] = matrix[i][j]

        piece.x += 1


class RotateClockwiseMove(Move):
    def execute(self, board, piece):
        pass


class RotateCounterClockwiseMove(Move):
    def execute(self, board, piece):
        pass
