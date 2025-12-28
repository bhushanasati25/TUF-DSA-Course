class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import defaultdict
        
        index_map = {num: i for i, num in enumerate(arr)}  
        n = len(arr)
        dp = defaultdict(lambda: 2)  
        max_len = 0  

        for j in range(n):
            for i in range(j):
                x = arr[j] - arr[i]  
                if x in index_map and index_map[x] < i:  
                    k = index_map[x]
                    dp[i, j] = dp[k, i] + 1
                    max_len = max(max_len, dp[i, j])

        return max_len if max_len >= 3 else 0  
