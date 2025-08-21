class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        if not mat or not mat[0]:
            return 0

        m, n = len(mat), len(mat[0])
        heights = [0] * n
        total = 0

        for r in range(m):
            # Update histogram heights for this row
            for c in range(n):
                heights[c] = heights[c] + 1 if mat[r][c] == 1 else 0

            # Monotonic increasing stack: (height, count_of_columns_merged)
            stack = []
            row_contrib = 0
            for h in heights:
                cnt = 1
                # Merge with previous >= heights to maintain increasing order
                while stack and stack[-1][0] >= h:
                    ph, pc = stack.pop()
                    row_contrib -= ph * pc
                    cnt += pc
                stack.append((h, cnt))
                row_contrib += h * cnt
                total += row_contrib

        return total
