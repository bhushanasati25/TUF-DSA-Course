class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        n = len(nums)
        d = [0] * (n + 1)
        for l, r in queries:
            d[l]   += 1
            d[r+1] -= 1
        s = 0
        for i, num in enumerate(nums):
            s += d[i]
            if num > s:
                return False

        return True
