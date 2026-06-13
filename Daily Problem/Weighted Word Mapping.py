class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        res = []
        for word in words:
            total_weight = sum(weights[ord(c) - ord('a')] for c in word)
            res.append(chr(ord('z') - (total_weight % 26)))
        return "".join(res)