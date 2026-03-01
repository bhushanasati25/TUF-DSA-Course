"""
🔗 Problem: Number of Steps to Reduce a Number in Binary Representation to One
📂 Category: Math-and-Counting
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

📝 Description:
   Steps to reduce binary string to '1' using add/divide rules.
"""

class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        steps = 0
        carry = 0

        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i])

            if bit + carry == 1:
                steps += 2
                carry = 1
            else:
                steps += 1

        return steps + carry