"""
🔗 Problem: Find the K-th Character in String Game I
📂 Category: Strings
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

📝 Description:
   Find kth character after repeatedly appending incremented copies.
"""

class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        # Count the number of 1's in binary representation of (k - 1)
        bit_count = bin(k - 1).count('1')
        # Return the corresponding character by shifting 'a' by bit_count
        return chr(ord('a') + bit_count)
