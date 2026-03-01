"""
🔗 Problem: Bitwise ORs of Subarrays
📂 Category: Math-and-Counting
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/bitwise-ors-of-subarrays/

📝 Description:
   Find number of distinct bitwise ORs of all subarrays.
"""

class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result = set()
        curr = set()

        for num in arr:
            # New set: bitwise OR of num with all elements in curr, plus num itself
            curr = {num | x for x in curr} | {num}
            result |= curr  # union with result set to track all unique ORs

        return len(result)
