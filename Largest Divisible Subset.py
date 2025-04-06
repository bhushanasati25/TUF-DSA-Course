class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        nums.sort()
        n = len(nums)
    
        dp = [1] * n  
        prev = [-1] * n  
        max_idx = 0  # To track the index of the largest subset's last element
        
        # Build up the dp and prev arrays.
        for i in range(n):
            for j in range(i):
                # Check if the current number is divisible by nums[j]
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            # Update max_idx if we found a larger subset ending at i.
            if dp[i] > dp[max_idx]:
                max_idx = i
        
        # Reconstruct the largest divisible subset.
        result = []
        while max_idx != -1:
            result.append(nums[max_idx])
            max_idx = prev[max_idx]
        
        return result[::-1]  # Reverse the list to get the correct order
