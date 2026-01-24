class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        max_sum = 0
        n = len(nums)
        
        for i in range(n // 2):
            current_pair_sum = nums[i] + nums[n - 1 - i]
            
            if current_pair_sum > max_sum:
                max_sum = current_pair_sum
                
        return max_sum