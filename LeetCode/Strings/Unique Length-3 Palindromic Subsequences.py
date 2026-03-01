"""
🔗 Problem: Unique Length-3 Palindromic Subsequences
📂 Category: Strings
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

📝 Description:
   Count unique palindromic subsequences of length 3.
"""

class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        first = [-1] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i

        ans = 0
    
        for c in range(26):
            if first[c] != -1 and first[c] < last[c]:
                l = first[c] + 1
                r = last[c]
                ans += len(set(s[l:r]))

        return ans
