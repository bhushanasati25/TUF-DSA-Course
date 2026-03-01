"""
🔗 Problem: Minimum Deletions to Make String Balanced
📂 Category: Strings
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

📝 Description:
   Min deletions to make string with all 'a's before all 'b's.
"""

class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """

        deletions = 0   
        b_count = 0    

        for ch in s:
            if ch == 'b':
                b_count += 1
            else:
                deletions = min(deletions + 1, b_count)

        return deletions
