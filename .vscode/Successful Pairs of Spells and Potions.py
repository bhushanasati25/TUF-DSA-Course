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
