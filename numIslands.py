"""
Given a 2d grid map of '1's (land) and '0's (water), 
count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
"""


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        height = len(grid)
        if height <= 0:
            return 0

        width = len(grid[0])
        if width <= 0:
            return 0

        def dfs(x, y):
            if x < 0 or x >= width or y < 0 or y >= height:
                return
            if grid[y][x] == '0':
                return
            grid[y][x] = '0'

            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        count = 0
        for x in range(width):
            for y in range(height):
                if grid[y][x] == '1':
                    count += 1
                    dfs(x, y)

        return count


def main():
    test = [["1", "1"]]
    print(Solution().numIslands(test))


if __name__ == '__main__':
    main()
