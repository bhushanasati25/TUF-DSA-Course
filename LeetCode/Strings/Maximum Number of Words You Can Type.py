"""
🔗 Problem: Maximum Number of Words You Can Type
📂 Category: Strings
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/maximum-number-of-words-you-can-type/

📝 Description:
   Count words typeable given a set of broken keys.
"""

class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        broken = set(brokenLetters)
        count = 0
        for w in text.split():
            if set(w).isdisjoint(broken):
                count += 1
        return count
