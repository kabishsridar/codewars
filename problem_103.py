"""
Given a Sudoku data structure with size NxN, N > 0 and √N == integer, write a method to validate if it has been filled out correctly.

The data structure is a multi-dimensional Array, i.e:

[
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],
  
  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],
  
  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]
Rules for validation

Data structure dimension: NxN where N > 0 and √N == integer
Rows may only contain integers: 1..N (N included)
Columns may only contain integers: 1..N (N included)
'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)
"""
import math

class Sudoku:
    def __init__(self, board):
        self.board = board
        self.size = len(board)
        self.box_size = int(math.sqrt(self.size))

    def check_list(self, numbers):
        if len(numbers) != self.size:
            return False
        if any(type(n) is not int or n < 1 or n > self.size for n in numbers):
            return False
        return set(numbers) == set(range(1, self.size + 1))

    def is_valid(self):
        if self.size == 0 or any(len(row) != self.size for row in self.board):
            return False
        if self.box_size ** 2 != self.size:
            return False

        for row in self.board:
            if not self.check_list(row):
                return False

        for j in range(self.size):
            column = [self.board[i][j] for i in range(self.size)]
            if not self.check_list(column):
                return False

        for row_start in range(0, self.size, self.box_size):
            for col_start in range(0, self.size, self.box_size):
                box = []
                for i in range(self.box_size):
                    for j in range(self.box_size):
                        box.append(self.board[row_start + i][col_start + j])
                if not self.check_list(box):
                    return False

        return True