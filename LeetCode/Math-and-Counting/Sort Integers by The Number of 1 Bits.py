"""
🔗 Problem: Sort Integers by The Number of 1 Bits
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

📝 Description:
   Sort integers by number of 1-bits, then by value.
"""

class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))