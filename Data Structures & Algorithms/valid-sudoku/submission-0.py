class Solution:

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """"""
        board_size=len(board[0])

        vertical_board=self.list_vertical(board)
        if not self.is_valid_sudoku_list(vertical_board) or not self.is_valid_sudoku_list(board):
            return False
        for row_start in range(0, board_size, 3):
            for col_start in range(0, board_size, 3):
                square=self.get_square(board, row_start, col_start)
                if not self.is_valid_square(square):
                    return False
        return True

    def is_valid_sudoku_list(self, board):
        for inner_list in board:
            if not self._count_sudoku_list(inner_list):
                return False
        return True

    def list_vertical(self, board:list[list]):
        zipped = zip(*board)
        result=[]
        for j in zipped:
            result.append(list(j))
        return result

    def _count_sudoku_list(self, items:list):
        """"""
        column_count = Counter(item for item in items if item not in ['.'])
        try:column_count.pop('.')
        except KeyError: pass
        if any(number > 1 for number in column_count.values()):
            return False
        return True

    def get_square(self, board, row_start, col_start):
        return [board[r][c] for r in range(row_start, row_start+3) for c in range(col_start, col_start+3)]

    def is_valid_square(self, square):
        """"""
        dictionary = Counter(item for item in square if item != '.')
        if any(number > 1 for number in dictionary.values()):
            return False
        return True