class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = sum(nums)
        
        current_F = sum(i * num for i, num in enumerate(nums))
        max_F = current_F
        
        for k in range(1, n):
            current_F = current_F + total_sum - n * nums[n - k]
            max_F = max(max_F, current_F)
            
        return max_F
        