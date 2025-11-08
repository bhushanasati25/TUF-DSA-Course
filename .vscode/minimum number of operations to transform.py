class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n:
            ans ^= n
            n >>= 1
        return ans
