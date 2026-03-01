"""
🔗 Problem: Convert Integer to the Sum of Two No-Zero Integers
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

📝 Description:
   Split integer into two positive integers without digit 0.
"""

class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def has_zero(x):
            # check if number contains digit '0'
            return '0' in str(x)
        
        for a in range(1, n):
            b = n - a
            if not has_zero(a) and not has_zero(b):
                return [a, b]
