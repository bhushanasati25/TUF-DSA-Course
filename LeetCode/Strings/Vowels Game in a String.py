"""
🔗 Problem: Vowels Game in a String
📂 Category: Strings
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/vowels-game-in-a-string/

📝 Description:
   Determine winner of game based on vowel positions.
"""

class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = set("aeiou")
        # Alice wins if there is at least one vowel
        return any(c in vowels for c in s)
