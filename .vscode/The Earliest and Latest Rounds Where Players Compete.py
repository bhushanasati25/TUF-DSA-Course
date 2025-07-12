class Solution(object):
    def earliestAndLatest(self, n, firstPlayer, secondPlayer):
        """
        :type n: int
        :type firstPlayer: int
        :type secondPlayer: int
        :rtype: List[int]
        """
        # Use explicit memoization since functools.lru_cache may not be available
        memo = {}
        def dp(l, r, k):
            # If they meet this round
            if l == r:
                return (1, 1)
            # Normalize positions
            if l > r:
                return dp(r, l, k)
            key = (l, r, k)
            if key in memo:
                return memo[key]
            earliest, latest = float('inf'), float('-inf')
            half = (k + 1) // 2
            # Enumerate all ways they both survive without meeting
            for i in range(1, l + 1):
                for j in range(l - i + 1, r - i + 1):
                    s = i + j
                    # Check valid survivor positions and that they didn't face off
                    if not (l + r - k//2 <= s <= half):
                        continue
                    x, y = dp(i, j, half)
                    earliest = min(earliest, x + 1)
                    latest = max(latest, y + 1)
            memo[key] = (earliest, latest)
            return memo[key]

        # Map secondPlayer to its position from the end
        l0 = firstPlayer
        r0 = n - secondPlayer + 1
        a, b = dp(l0, r0, n)
        return [a, b]
