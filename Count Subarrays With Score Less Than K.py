class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        left = 0
        total = 0
        window_sum = 0
        
        for right in range(n):
            window_sum += nums[right]
            while window_sum * (right - left + 1) >= k:
                window_sum -= nums[left]
                left += 1
            total += (right - left + 1)
        
        return total
