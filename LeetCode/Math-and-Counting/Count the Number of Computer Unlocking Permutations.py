"""
🔗 Problem: Count the Number of Computer Unlocking Permutations
📂 Category: Math-and-Counting
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

📝 Description:
   Count permutations where first computer is unlocked first.
"""

class Solution(object):
    def countPermutations(self, complexity):
        """
        :type complexity: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(complexity)
        if n <= 1:
            return 1
        
        root = complexity[0]
        for i in range(1, n):
            if complexity[i] <= root:
                return 0
    
        res = 1
        for k in range(2, n): 
            res = (res * k) % MOD
        return res
