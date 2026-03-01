"""
🔗 Problem: Taking Maximum Energy From the Mystic Dungeon
📂 Category: Dynamic-Programming
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

📝 Description:
   Find max energy starting from any position with k-step jumps.
"""

class Solution(object):
    def maximumEnergy(self, energy, k):
        """
        :type energy: List[int]
        :type k: int
        :rtype: int
        """
        n = len(energy)
        dp = energy[:]              
        for i in range(n - 1 - k, -1, -1):
            dp[i] += dp[i + k]
        return max(dp)
