"""
🔗 Problem: Find Words Containing Character
📂 Category: Strings
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/find-words-containing-character/

📝 Description:
   Find indices of words containing a given character.
"""

class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        result = []
        
        for i, word in enumerate(words):
            if x in word:
                result.append(i)
        
        return result
