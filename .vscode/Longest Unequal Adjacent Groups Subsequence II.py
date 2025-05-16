class Solution(object):
    def getWordsInLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        n = len(words)
        dp = [1] * n
        prev = [-1] * n

        # Helper function to compute Hamming distance
        def hamming_dist(w1, w2):
            if len(w1) != len(w2):
                return -1
            return sum(c1 != c2 for c1, c2 in zip(w1, w2))

        # Build DP array
        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]) and hamming_dist(words[i], words[j]) == 1:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j

        # Find the index of the last element in the longest subsequence
        max_len = max(dp)
        max_index = dp.index(max_len)

        # Reconstruct the subsequence
        result = []
        while max_index != -1:
            result.append(words[max_index])
            max_index = prev[max_index]

        result.reverse()
        return result
