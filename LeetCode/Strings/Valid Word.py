"""
🔗 Problem: Valid Word
📂 Category: Strings
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/valid-word/

📝 Description:
   Check if string is a valid word with vowels and consonants.
"""

class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            return False

        vowels = set("aeiouAEIOU")
        hasVowel = False
        hasConsonant = False

        for ch in word:
            if not ch.isalnum():
                return False
            if ch.isalpha():
                if ch in vowels:
                    hasVowel = True
                else:
                    hasConsonant = True

        return hasVowel and hasConsonant
