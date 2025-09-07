class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(1, n // 2 + 1):
            res.extend([i, -i])
        if n % 2 == 1:
            res.append(0)
        return res
