"""
🔗 Problem: Successful Pairs of Spells and Potions
📂 Category: Binary-Search
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

📝 Description:
   Count successful spell-potion pairs with product ≥ success.
"""

import bisect

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        n = len(potions)
        res = []
        for s in spells:
            if s <= 0:
                res.append(0)
                continue
            need = (success + s - 1) // s  # ceil(success / s)
            idx = bisect.bisect_left(potions, need)
            res.append(n - idx)
        return res
