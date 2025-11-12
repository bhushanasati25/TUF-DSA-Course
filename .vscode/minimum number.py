from fractions import gcd

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        ones = sum(1 for x in nums if x == 1)
        if ones:
            return n - ones

        best = float('inf')
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    best = min(best, j - i + 1)
                    break

        if best == float('inf'):
            return -1

        return (best - 1) + (n - 1)