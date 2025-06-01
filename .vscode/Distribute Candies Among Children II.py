class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
    
        def ways(m):
            if m < 0:
                return 0
            return (m + 2) * (m + 1) // 2

        if n > 3 * limit:
            return 0

        t = limit + 1
        total = ways(n)
        total -= 3 * ways(n - t)
        total += 3 * ways(n - 2 * t)
        total -= ways(n - 3 * t)
        return total
