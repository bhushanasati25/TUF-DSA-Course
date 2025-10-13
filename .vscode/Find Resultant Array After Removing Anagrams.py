class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        prev_sig = None

        for w in words:
            freq = [0] * 26
            for ch in w:
                freq[ord(ch) - ord('a')] += 1
            sig = tuple(freq)
            if sig != prev_sig:
                res.append(w)
                prev_sig = sig

        return res
