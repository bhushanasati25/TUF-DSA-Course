class Solution(object):
    def maxOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        ones = 0
        n = len(s)

        for i, c in enumerate(s):
            if c == '1':
                ones += 1
            else: 
                if i + 1 == n or s[i + 1] == '1':
                    ans += ones

        return ans
