class TicTacToe:
    def __init__(self):
        self.board = ['*' for _ in range(9)]  # single list to represent 3x3 board
        self.current_winner = None  # keeps track of winner

    def print_board(self):
        board = [self.board[i * 3:(i + 1) * 3] for i in range(3)]
        for row in board:
            print(' | '.join(row))
            print('---' * 3)

    @staticmethod
    def numbers_for_tiles():
        """This method helps us to visualize which number to each tile"""
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print(' | '.join(row))
            print('---' * 3)

    def available_moves(self):
        """list of all available moves"""
        # This is a normal way
        # moves = []
        # for idx, elem in enumerate(self.board):
        #     if elem == '*':
        #         moves.append(idx)
        # return moves
        return [idx for idx, element in enumerate(self.board) if element == '*']

    def any_empty_squares(self):
        """returns Boolean if any empty squares remaining"""
        return '*' in self.board

    def count_empty_squares(self):
        """count of empty squares"""
        return self.board.count('*')

    def make_move(self, tile, letter):
        """Function to make a move if valid"""
        if self.board[tile] == '*':
            self.board[tile] = letter
            if self.winner(tile, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, tile, letter):
        # first check the row
        row_ind = tile // 3
        rows = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all([item == letter for item in rows]):
            return True

        col_ind = tile % 3
        cols = [self.board[col_ind+(i*3)] for i in range(3)]
        if all([item == letter for item in cols]):
            return True

        if tile % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([item == letter for item in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([item == letter for item in diagonal2]):
                return True

        return False
