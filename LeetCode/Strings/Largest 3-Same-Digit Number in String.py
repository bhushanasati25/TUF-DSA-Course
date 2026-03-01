"""
🔗 Problem: Largest 3-Same-Digit Number in String
📂 Category: Strings
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/largest-3-same-digit-number-in-string/

📝 Description:
   Find largest good integer (3 same consecutive digits) in string.
"""

class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        largest = ""
        for i in range(len(num) - 2):
            # Check if three consecutive digits are the same
            if num[i] == num[i+1] == num[i+2]:
                # Update largest if this triplet is greater
                largest = max(largest, num[i:i+3])
        return largest
