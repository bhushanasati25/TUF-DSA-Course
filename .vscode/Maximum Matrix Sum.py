class Solution:
    def maxMatrixSum(self, matrix):
        total = 0
        negative_count = 0
        min_abs_val = float('inf')

        for row in matrix:
            for x in row:
                if x < 0:
                    negative_count += 1
                total += abs(x)
                min_abs_val = min(min_abs_val, abs(x))

        if negative_count % 2 != 0:
            total -= 2 * min_abs_val

        return total
