class Solution(object):
    def numMagicSquaresInside(self, grid):
        rows, cols = len(grid), len(grid[0])
        count = 0

        def isMagic(r, c):
            if grid[r+1][c+1] != 5:
                return False
            nums = set()
            for i in range(r, r+3):
                for j in range(c, c+3):
                    val = grid[i][j]
                    if val < 1 or val > 9:
                        return False
                    nums.add(val)

            if len(nums) != 9:
                return False

            s = 15
            for i in range(3):
                if sum(grid[r+i][c:c+3]) != s:
                    return False

            # Columns
            for j in range(3):
                if grid[r][c+j] + grid[r+1][c+j] + grid[r+2][c+j] != s:
                    return False

            # Diagonals
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != s:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != s:
                return False

            return True

        for i in range(rows - 2):
            for j in range(cols - 2):
                if isMagic(i, j):
                    count += 1

        return count
