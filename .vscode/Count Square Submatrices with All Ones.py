class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        prev = [0] * (n + 1)  # dp for previous row
        ans = 0

        for i in range(1, m + 1):
            cur = [0] * (n + 1)
            for j in range(1, n + 1):
                if matrix[i-1][j-1] == 1:
                    cur[j] = 1 + min(prev[j], cur[j-1], prev[j-1])
                    ans += cur[j]
            prev = cur

        return ans
