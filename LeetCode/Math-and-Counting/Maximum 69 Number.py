"""
🔗 Problem: Maximum 69 Number
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/maximum-69-number/

📝 Description:
   Change at most one digit 6 to 9 to get maximum number.
"""

class Solution(object):
    def maximum69Number(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Convert to string, replace the first '6' with '9', and convert back
        return int(str(num).replace('6', '9', 1))
