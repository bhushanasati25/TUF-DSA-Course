"""
🔗 Problem: Zigzag Conversion
📂 Category: Strings
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/zigzag-conversion/

📝 Description:
   Convert string to zigzag pattern on given rows, read line by line.
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        index, step = 0, 1

        for char in s:
            rows[index] += char
            
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1

            index += step

        return ''.join(rows)
