class Solution(object):
    def possibleStringCount(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Step 1: Parse the word into groups of repeated characters
        groups = []
        i = 0
        while i < len(word):
            j = i
            while i < len(word) and word[i] == word[j]:
                i += 1
            groups.append(i - j)
        
        # Step 2: Compute total possible original strings
        total = 1
        for g in groups:
            total = (total * g) % MOD
        
        n = len(groups)
        if n >= k:
            return total
        
        # Step 3: Dynamic Programming to count invalid strings (length < k)
        dp = [0] * k
        dp[0] = 1
        
        for g in groups:
            prefix_sum = [0] * (k + 1)
            for i in range(k):
                prefix_sum[i + 1] = (prefix_sum[i] + dp[i]) % MOD
            new_dp = [0] * k
            for i in range(1, k):
                l = max(0, i - g)
                r = i
                new_dp[i] = (prefix_sum[r] - prefix_sum[l] + MOD) % MOD
            dp = new_dp
        
        invalid = sum(dp) % MOD
        return (total - invalid + MOD) % MOD
