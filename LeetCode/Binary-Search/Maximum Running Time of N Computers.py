"""
🔗 Problem: Maximum Running Time of N Computers
📂 Category: Binary-Search
🎯 Difficulty: Hard
🔗 URL: https://leetcode.com/problems/maximum-running-time-of-n-computers/

📝 Description:
   Find max time n computers can run simultaneously with batteries.
"""

class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        def can_run(t):
            total = 0
            need = n * t
            for b in batteries:
                total += b if b < t else t
                if total >= need:
                    return True
            return total >= need

        lo, hi = 0, sum(batteries) // n
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_run(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
