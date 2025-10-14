class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if 2 * k > n:
            return False

        # run[i] = length of strictly increasing run starting at i
        run = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                run[i] = run[i + 1] + 1

        # check adjacent windows [i, i+k-1] and [i+k, i+2k-1]
        for i in range(0, n - 2 * k + 1):
            if run[i] >= k and run[i + k] >= k:
                return True
        return False
