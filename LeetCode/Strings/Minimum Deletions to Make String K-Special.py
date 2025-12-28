class Solution(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        from collections import Counter

        freq = Counter(word).values()
        freq = list(freq)
        min_deletions = float('inf')

        for base in range(max(freq) + 1):
            deletions = 0
            for f in freq:
                if f < base:
                    deletions += f  # delete all occurrences
                elif f > base + k:
                    deletions += f - (base + k)
            min_deletions = min(min_deletions, deletions)

        return min_deletions
