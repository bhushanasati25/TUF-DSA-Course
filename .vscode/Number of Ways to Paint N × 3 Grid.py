class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        typeA = 6
        typeB = 6

        for _ in range(1, n):
            newA = (typeA * 3 + typeB * 2) % MOD
            newB = (typeA * 2 + typeB * 2) % MOD
            typeA, typeB = newA, newB

        return (typeA + typeB) % MOD
