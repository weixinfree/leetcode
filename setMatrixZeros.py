class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        if not matrix:
            return

        height = len(matrix)
        width = len(matrix[0])

        def x_zeros(x):
            for i in range(height):
                matrix[i][x] = 0

        def y_zeros(y):
            a = matrix[y]
            for i in range(len(a)):
                a[i] = 0

        pos = [(x,y) for x in range(width) for y in range(height) if matrix[y][x] == 0]
        xs = {x for x,_ in pos}
        ys = {y for _,y in pos}

        [x_zeros(x) for x in xs]
        [y_zeros(y) for y in ys]


def main():
    matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    Solution().setZeroes(matrix)
    print(matrix)


if __name__ == '__main__':
    main()
