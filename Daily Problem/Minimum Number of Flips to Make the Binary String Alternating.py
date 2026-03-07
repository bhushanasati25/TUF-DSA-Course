class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        s = s + s

        diff1 = 0
        diff2 = 0
        res = float('inf')
        left = 0

        for right in range(len(s)):
            if right % 2 == 0:
                if s[right] != '0':
                    diff1 += 1
                if s[right] != '1':
                    diff2 += 1
            else:
                if s[right] != '1':
                    diff1 += 1
                if s[right] != '0':
                    diff2 += 1

            if right - left + 1 > n:
                if left % 2 == 0:
                    if s[left] != '0':
                        diff1 -= 1
                    if s[left] != '1':
                        diff2 -= 1
                else:
                    if s[left] != '1':
                        diff1 -= 1
                    if s[left] != '0':
                        diff2 -= 1
                left += 1

            if right - left + 1 == n:
                res = min(res, diff1, diff2)

        return res