"""
🔗 Problem: 1-bit and 2-bit Characters
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/1-bit-and-2-bit-characters/

📝 Description:
   Check if last character is a one-bit character (0).
"""

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        n = len(bits)
        while i < n - 1:
            if bits[i] == 1:
                i += 2   # 2-bit character
            else:
                i += 1   # 1-bit character
        return i == n - 1
