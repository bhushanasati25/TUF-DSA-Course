class Solution(object):
    def flowerGame(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        # Alice wins iff the two numbers have different parity.
        # Count of such pairs = floor(n*m/2).
        return (n * m) // 2
