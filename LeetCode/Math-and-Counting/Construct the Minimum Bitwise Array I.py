"""
🔗 Problem: Construct the Minimum Bitwise Array I
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

📝 Description:
   Find array where OR with right-shifted self equals given values.
"""

class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        
        for x in nums:
            if x == 2:
                ans.append(-1)
            else:
                bit = 0
                while (x >> bit) & 1:
                    bit += 1
                ans.append(x - (1 << (bit - 1)))
                
        return ans