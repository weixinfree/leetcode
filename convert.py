class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows < 2:
            return s

        matrix = []
        z_index = 0
        z_range = numRows - 2

        Split = numRows + z_range

        for index, v in enumerate(s):
            pos = index % Split
            carry = index // Split

            edge_index = (numRows - 1) * carry
            if pos < numRows:
                matrix.append((pos, edge_index, v))
            else:
                delt = pos - numRows
                z_index = edge_index + delt + 1
                matrix.append((numRows - delt - 2, z_index, v))

        matrix.sort()
        return ''.join(item[2] for item in matrix)


def _print_matrix(m):
    ROW = max(item.row for item in m) + 1
    COL = max(item.col for item in m) + 1
    matrix = [['*' for _ in range(COL)] for _ in range(ROW)]

    for row, col, v in m:
        print(row, col, v)
        matrix[row][col] = v

    for row in range(ROW):
        for col in range(COL):
            print(matrix[row][col], end='')
        print()


def _assert(get, expect):
    print(f'got: {get}, expect: {expect}')
    assert expect == get


if __name__ == "__main__":
    s = Solution()
    _assert(s.convert("LEETCODEISHIRING", 3), "LCIRETOESIIGEDHN")
    _assert(s.convert("LEETCODEISHIRING", 3), "LCIRETOESIIGEDHN")
    _assert(s.convert("LEETCODEISHIRING", 4), "LDREOEIIECIHNTSG")
    _assert(s.convert("A", 1), 'A')
    _assert(s.convert("ABC", 2), 'ACB')
