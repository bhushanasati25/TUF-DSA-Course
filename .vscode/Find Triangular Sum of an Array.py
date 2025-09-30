class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Iteratively reduce the array until one element remains
        for end in range(n - 1, 0, -1):
            for i in range(end):
                nums[i] = (nums[i] + nums[i + 1]) % 10
        return nums[0]
