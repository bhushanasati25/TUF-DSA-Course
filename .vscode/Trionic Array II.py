class Solution(object):
    def maxSumTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = float('-inf')
        i = 0
        
        while i < n:
            l = i
            i += 1
            
            while i < n and nums[i - 1] < nums[i]:
                i += 1
            
            if i == l + 1:
                continue
            
            p = i - 1  
            curr_sum = nums[p - 1] + nums[p]

            while i < n and nums[i - 1] > nums[i]:
                curr_sum += nums[i]
                i += 1
            
            if i == p + 1 or i == n or nums[i - 1] == nums[i]:
                continue
            
            q = i - 1 
            curr_sum += nums[i]
            i += 1
            
            max_right_extension = 0
            temp_sum = 0
            
            while i < n and nums[i - 1] < nums[i]:
                temp_sum += nums[i]
                max_right_extension = max(max_right_extension, temp_sum)
                i += 1
            
            curr_sum += max_right_extension
            
            max_left_extension = 0
            temp_sum = 0
            j = p - 2
            
            while j >= l:
                temp_sum += nums[j]
                max_left_extension = max(max_left_extension, temp_sum)
                j -= 1
            
            curr_sum += max_left_extension
            ans = max(ans, curr_sum)
            i = q
        
        return ans