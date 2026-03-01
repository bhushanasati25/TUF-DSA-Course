"""
🔗 Problem: Check If All 1's Are at Least Length K Places Away
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

📝 Description:
   Check if all 1s in array are at least k positions apart.
"""

class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prev_one = -1   
        
        for i, val in enumerate(nums):
            if val == 1:
                if prev_one != -1 and i - prev_one - 1 < k:
                    return False
                prev_one = i  
                
        return True
