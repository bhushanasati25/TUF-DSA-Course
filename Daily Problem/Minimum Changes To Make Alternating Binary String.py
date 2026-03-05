class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        n = len(s)
        
        for i in range(n):
            if int(s[i]) != i % 2:
                count += 1
        return min(count, n - count)