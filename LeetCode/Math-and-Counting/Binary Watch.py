"""
🔗 Problem: Binary Watch
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/binary-watch/

📝 Description:
   Return all possible times a binary watch could display.
"""

class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        result = []

        for hour in range(12):
            for minute in range(60):
                hour_bits = bin(hour).count('1')
                minute_bits = bin(minute).count('1')

                if hour_bits + minute_bits == turnedOn:
                    time = "{}:{:02d}".format(hour, minute)
                    result.append(time)

        return result