"""
🔗 Problem: Check If Digits Are Equal in String After Operations I
📂 Category: Strings
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

📝 Description:
   Check if repeated digit-summing operations make all digits equal.
"""

class Solution(object):
    def hasSameDigits(self, s):
        a = [ord(c) - 48 for c in s]
        while len(a) > 2:
            a = [(a[i] + a[i+1]) % 10 for i in range(len(a)-1)]
        return a[0] == a[1]
