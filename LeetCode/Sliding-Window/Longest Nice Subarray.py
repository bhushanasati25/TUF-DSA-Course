"""
🔗 Problem: Longest Nice Subarray
📂 Category: Sliding-Window
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/longest-nice-subarray/

📝 Description:
   Find longest subarray where all pairs have AND = 0.
"""

class Solution(object):
    def longestNiceSubarray(self, nums):
        l = 0
        current_mask = 0
        max_len = 0
        
        for r, num in enumerate(nums):
            while (current_mask & num) != 0:
                current_mask ^= nums[l]
                l += 1
            current_mask |= num
            max_len = max(max_len, r - l + 1)
        
        return max_len
