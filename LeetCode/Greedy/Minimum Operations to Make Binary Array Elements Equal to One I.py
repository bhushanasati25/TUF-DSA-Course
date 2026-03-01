"""
🔗 Problem: Minimum Operations to Make Binary Array Elements Equal to One I
📂 Category: Greedy
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/

📝 Description:
   Min flips of 3 consecutive elements to make binary array all ones.
"""

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i, x in enumerate(nums):
            if x == 0:
                if i + 2 >= len(nums):
                    return -1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                ans += 1
        return ans