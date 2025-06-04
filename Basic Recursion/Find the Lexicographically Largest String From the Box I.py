class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        n = len(word)
        if numFriends == 1:
            return word

        L = n - numFriends + 1

        i, j, k = 0, 1, 0
        while j + k < n:
            if word[i + k] == word[j + k]:
                k += 1
            elif word[i + k] > word[j + k]:
                j = j + k + 1
                k = 0
            else:
                i = max(i + k + 1, j)
                j = i + 1
                k = 0


        suffix = word[i:]
        return suffix[:L]
