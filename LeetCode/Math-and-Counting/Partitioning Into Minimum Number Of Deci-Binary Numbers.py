"""
🔗 Problem: Partitioning Into Minimum Number Of Deci-Binary Numbers
📂 Category: Math-and-Counting
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

📝 Description:
   Min deci-binary numbers that sum to given number.
"""

class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        max_digit = 0
        
        for digit in n:
            max_digit = max(max_digit, int(digit))
        
        return max_digit