"""
🔗 Problem: Number of Laser Beams in a Bank
📂 Category: Math-and-Counting
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

📝 Description:
   Count laser beams between consecutive rows with security devices.
"""

class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        ans = 0
        prev = 0  # stores the number of '1's in the previous non-empty row
        
        for row in bank:
            count = row.count('1')
            if count == 0:
                continue
            ans += prev * count
            prev = count
        
        return ans
