"""
🔗 Problem: Final Value of Variable After Performing Operations
📂 Category: Arrays
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

📝 Description:
   Simulate ++X, X++, --X, X-- operations and return final value.
"""

class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0
        for op in operations:
            if '+' in op:
                x += 1
            else:
                x -= 1
        return x
