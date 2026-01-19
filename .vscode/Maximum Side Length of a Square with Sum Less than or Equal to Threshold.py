class Solution(object):
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])

        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    mat[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )

        def canForm(k):
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    total = (
                        prefix[i][j]
                        - prefix[i - k][j]
                        - prefix[i][j - k]
                        + prefix[i - k][j - k]
                    )
                    if total <= threshold:
                        return True
            return False

        low, high = 0, min(m, n)

        while low < high:
            mid = (low + high + 1) // 2
            if canForm(mid):
                low = mid
            else:
                high = mid - 1

        return low
