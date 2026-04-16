class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        n = len(words)
        min_dist = n
        
        for i, word in enumerate(words):
            if word == target:
                dist = abs(i - startIndex)
                min_dist = min(min_dist, dist, n - dist)
                
        return min_dist if min_dist != n else -1