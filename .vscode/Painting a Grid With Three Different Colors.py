class Solution(object):
    def colorTheGrid(self, m, n):
        MOD = 10**9 + 7
        colors = [0, 1, 2]

        # Generate all valid column states
        def generate_columns():
            def backtrack(row, path):
                if row == m:
                    valid.append(tuple(path))
                    return
                for color in colors:
                    if row > 0 and path[-1] == color:
                        continue
                    path.append(color)
                    backtrack(row + 1, path)
                    path.pop()

            valid = []
            backtrack(0, [])
            return valid

        valid_cols = generate_columns()

        # Check which column states are compatible
        compatible = {}
        for c1 in valid_cols:
            compatible[c1] = []
            for c2 in valid_cols:
                if all(a != b for a, b in zip(c1, c2)):
                    compatible[c1].append(c2)

        # DP with memoization using dictionary
        memo = {}

        def dp(i, prev):
            if i == n:
                return 1
            if (i, prev) in memo:
                return memo[(i, prev)]

            total = 0
            for nxt in compatible[prev]:
                total = (total + dp(i + 1, nxt)) % MOD

            memo[(i, prev)] = total
            return total

        # Try all starting columns
        result = 0
        for col in valid_cols:
            result = (result + dp(1, col)) % MOD

        return result
