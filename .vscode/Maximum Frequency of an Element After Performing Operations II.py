from bisect import bisect_left, bisect_right
from collections import Counter

class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        """
        :type nums: List[int]
        :type k: int
        :type numOperations: int
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n

        L = [x - k for x in nums]
        R = [x + k for x in nums]
        L.sort()
        R.sort()

        i = j = 0
        cur = M = 0
        while i < n and j < n:
            if L[i] <= R[j]:
                cur += 1
                M = max(M, cur)
                i += 1
            else:
                cur -= 1
                j += 1

        ans = min(M, numOperations)

        freq = Counter(nums)
        distinct = sorted(freq.keys())
        for t in distinct:
            cover = bisect_right(L, t) - bisect_left(R, t)
            ans = max(ans, min(cover, freq[t] + numOperations))

        return ans
