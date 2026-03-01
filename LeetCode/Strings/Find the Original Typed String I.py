"""
🔗 Problem: Find the Original Typed String I
📂 Category: Strings
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/find-the-original-typed-string-i/

📝 Description:
   Count possible original strings before accidental key repeats.
"""

class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Start with 1 for the case where no long-press mistake occurred
        count = 1
        
        # For each consecutive pair, if they're identical,
        # that duplicate could be the extra long-press
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
        
        return count
