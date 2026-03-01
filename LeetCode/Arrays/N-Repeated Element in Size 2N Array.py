"""
🔗 Problem: N-Repeated Element in Size 2N Array
📂 Category: Arrays
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

📝 Description:
   Find the element repeated N times in an array of size 2N.
"""

class Solution(object):
    def repeatedNTimes(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
