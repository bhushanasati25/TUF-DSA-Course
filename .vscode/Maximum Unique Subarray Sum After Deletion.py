class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        if max_num <= 0:
            return max_num

        seen = set()
        total = 0
        for num in nums:
            if num > 0 and num not in seen:
                seen.add(num)
                total += num
        return total
