class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Count elements that are not divisible by 3
        return sum(1 for x in nums if x % 3 != 0)
