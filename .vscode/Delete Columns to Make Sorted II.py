class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs)
        m = len(strs[0])

        is_sorted = [False] * (n - 1)
        deletions = 0
        
        for col in range(m):
            must_delete = False
            for i in range(n - 1):
                if not is_sorted[i]:
                    if strs[i][col] > strs[i+1][col]:
                        must_delete = True
                        break
            
            if must_delete:
                deletions += 1
            else:
                for i in range(n - 1):
                    if not is_sorted[i] and strs[i][col] < strs[i+1][col]:
                        is_sorted[i] = True
                        
        return deletions