"""
🔗 Problem: Minimum Number of Increments on Subarrays to Form a Target Array
📂 Category: Dynamic-Programming
🎯 Difficulty: Hard
🔗 URL: https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/

📝 Description:
   Min operations to build target array by incrementing subarrays.
"""

class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        if not target:
            return 0
        ops = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                ops += target[i] - target[i - 1]
        return ops
