"""
🔗 Problem: Find Lucky Integer in an Array
📂 Category: Arrays
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/find-lucky-integer-in-an-array/

📝 Description:
   Find the largest integer whose frequency equals its value.
"""

class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import Counter

        freq = Counter(arr)
        lucky = -1

        for num in freq:
            if num == freq[num]:
                lucky = max(lucky, num)

        return lucky
