class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n

        for i in range(n):
            x = nums[i]

            if x == 0:
                result[i] = 0
            else:
                target = (i + x) % n
                result[i] = nums[target]

        return result
