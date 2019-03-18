from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def get(row: int, col: int) -> str:
            return board[row][col]

        def col(col: int) -> List[str]:
            return (get(i, col) for i in range(9))

        def row(row: int) -> List[str]:
            return board[row]

        def box(x: int, y: int) -> List[str]:
            col_range = range(x*3, (x + 1) * 3)
            row_range = range(y*3, (y + 1) * 3)

            return (get(row, col) for row in row_range for col in col_range)

        def is_valid(li):
            counts = set()
            for v in li:
                if v != '.' and v in counts:
                    return False
                counts.add(v)
            return True

        if not board:
            return False

        for i in range(9):
            if not is_valid(col(i)):
                print(f'invalid col: {i}')
                return False

        for i in range(9):
            if not is_valid(row(i)):
                print(f'invalid row: {i}')
                return False

        for x, y in ((x, y) for x in range(3) for y in range(3)):
            if not is_valid(box(x, y)):
                print(f'invalid box: ({x}, {y})')
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isValidSudoku([
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]))

    print('=' * 20)

    print(s.isValidSudoku([
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]))

    print('=' * 20)

    print(s.isValidSudoku([
        [".", ".", "4", ".", ".", ".", "6", "3", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["5", ".", ".", ".", ".", ".", ".", "9", "."],
        [".", ".", ".", "5", "6", ".", ".", ".", "."],
        ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
        [".", ".", ".", "7", ".", ".", ".", ".", "."],
        [".", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."]
    ]))
