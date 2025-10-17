class Solution(object):
    def maxPartitionsAfterOperations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        memo = {}

        def bit(c):
            return 1 << (ord(c) - 97)

        def dp(i, can_change, mask):
            key = (i, can_change, mask)
            if key in memo:
                return memo[key]
            if i == len(s):
                return 0

            b = bit(s[i])
            best = -10**9

            new_mask = mask | b
            if bin(new_mask).count("1") > k:
                best = max(best, 1 + dp(i + 1, can_change, b))
            else:
                best = max(best, dp(i + 1, can_change, new_mask))

            if can_change:
                if mask != 0:
                    best = max(best, dp(i + 1, 0, mask))
                for j in range(26):
                    nb = 1 << j
                    if mask & nb:
                        continue
                    nm = mask | nb
                    if bin(nm).count("1") > k:
                        best = max(best, 1 + dp(i + 1, 0, nb))
                    else:
                        best = max(best, dp(i + 1, 0, nm))

            memo[key] = best
            return best

        return dp(0, 1, 0) + 1
