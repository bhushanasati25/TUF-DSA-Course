"""
🔗 Problem: Check If a String Contains All Binary Codes of Size K
📂 Category: Math-and-Counting
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

📝 Description:
   Check if all binary strings of length k appear as substrings.
"""

class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        
        n = len(s)

        if n - k + 1 < (1 << k):
            return False

        seen = set()

        for i in range(n - k + 1):
            substring = s[i:i+k]
            seen.add(substring)

            if len(seen) == (1 << k):
                return True

        return False