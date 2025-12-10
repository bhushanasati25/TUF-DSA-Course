class Solution(object):
    def countPermutations(self, complexity):
        """
        :type complexity: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(complexity)
        if n <= 1:
            return 1
        
        root = complexity[0]
        for i in range(1, n):
            if complexity[i] <= root:
                return 0
    
        res = 1
        for k in range(2, n): 
            res = (res * k) % MOD
        return res
