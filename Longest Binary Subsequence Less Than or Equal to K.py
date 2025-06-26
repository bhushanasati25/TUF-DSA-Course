class Solution(object):
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        length = 0  # number of bits we’ve taken so far
        value = 0   # current integer value of that subsequence

        # Build subsequence from the least significant bit upward:
        for c in reversed(s):
            if c == '0':
                # zeros never increase the numeric value—always take them
                length += 1
            else:
                # only take a '1' if it still keeps us ≤ k
                # and we haven’t exceeded 30 bits (since k < 2^30)
                if length < 30 and (value | (1 << length)) <= k:
                    value |= (1 << length)
                    length += 1

        return length
