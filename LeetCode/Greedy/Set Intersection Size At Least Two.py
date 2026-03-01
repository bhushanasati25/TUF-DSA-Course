"""
🔗 Problem: Set Intersection Size At Least Two
📂 Category: Greedy
🎯 Difficulty: Hard
🔗 URL: https://leetcode.com/problems/set-intersection-size-at-least-two/

📝 Description:
   Find min set size so intersection with each interval ≥ 2.
"""

class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[1], -x[0]))

        a = -10**18
        b = -10**18
        ans = 0

        for l, r in intervals:
            if l > b:
                ans += 2
                a, b = r - 1, r
            elif l > a:
                ans += 1
                a, b = b, r
            else:
                pass

        return ans
