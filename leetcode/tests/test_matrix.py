import pytest
from leetcode.matrix.valid_sudoku import Solution as validSudoku_Solution

@pytest.mark.parametrize("board, expected", [
    (
        [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ], True
    ),
    (
        [
            ["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ], False
    ),
    (
        [
            ["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ], False
    ),
    (
        [
            [".","2",".",".",".",".",".",".","."],
            [".",".",".",".",".",".","5",".","1"],
            [".",".",".",".",".",".","8","1","3"],
            ["4",".","9",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".","2",".",".",".",".",".","."],
            ["7",".","6",".",".",".",".",".","."],
            ["9",".",".",".",".","4",".",".","."],
            [".",".",".",".",".",".",".",".","."]
        ], False
    )
])
def test_validSudoku(board, expected):
    solution = validSudoku_Solution()
    assert solution.isValidSudoku(board) == expected