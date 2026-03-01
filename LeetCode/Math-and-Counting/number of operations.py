"""
🔗 Problem: number of operations
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/number-of-operations/

📝 Description:
   Count operations to make two numbers equal by repeated subtraction.
"""

class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        count = 0
        while num1 and num2:
            if num1 >= num2:
                count += num1 // num2
                num1 %= num2
            else:
                count += num2 // num1
                num2 %= num1
        return count
