class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        res = []
        r = c = 0
        direction = 1  # 1 = up-right, -1 = down-left

        for _ in range(m * n):
            res.append(mat[r][c])
            if direction == 1:
                if c == n - 1:      # right wall -> go down
                    r += 1
                    direction = -1
                elif r == 0:        # top wall -> go right
                    c += 1
                    direction = -1
                else:               # move up-right
                    r -= 1
                    c += 1
            else:
                if r == m - 1:      # bottom wall -> go right
                    c += 1
                    direction = 1
                elif c == 0:        # left wall -> go down
                    r += 1
                    direction = 1
                else:               # move down-left
                    r += 1
                    c -= 1
        return res
