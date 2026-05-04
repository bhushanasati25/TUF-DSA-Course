class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(start, path):
            if len(path) == k:
                result.append(list(path))
                return
            
            limit = n - (k - len(path)) + 1
            for i in range(start, limit + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
                
        backtrack(1, [])
        return result