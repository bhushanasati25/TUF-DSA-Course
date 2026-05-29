class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = float('inf')
        
        for num in nums:
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num //= 10
            
            if digit_sum < min_val:
                min_val = digit_sum
                
        return min_val