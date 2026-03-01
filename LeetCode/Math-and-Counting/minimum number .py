"""
🔗 Problem: minimum number
📂 Category: Math-and-Counting
🎯 Difficulty: Hard
🔗 URL: https://leetcode.com/problems/minimum-number/

📝 Description:
   Minimum operations to make array contain 1, then spread to all.
"""

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        stack = [0]  
        for x in nums:
            while stack and stack[-1] > x:
                stack.pop()
            if not stack or stack[-1] < x:
                ans += 1
                stack.append(x)
        return ans
