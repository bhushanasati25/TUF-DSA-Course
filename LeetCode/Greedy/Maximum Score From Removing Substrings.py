"""
🔗 Problem: Maximum Score From Removing Substrings
📂 Category: Greedy
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/maximum-score-from-removing-substrings/

📝 Description:
   Max score removing 'ab' and 'ba' substrings with different points.
"""

class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        def remove_pair(s, first, second, score):
            stack = []
            points = 0
            for ch in s:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    points += score
                else:
                    stack.append(ch)
            return ''.join(stack), points
        
        total = 0
        # Always remove the higher-value pair first
        if x >= y:
            s, gain = remove_pair(s, 'a', 'b', x)
            total += gain
            _, gain = remove_pair(s, 'b', 'a', y)
            total += gain
        else:
            s, gain = remove_pair(s, 'b', 'a', y)
            total += gain
            _, gain = remove_pair(s, 'a', 'b', x)
            total += gain
            
        return total
