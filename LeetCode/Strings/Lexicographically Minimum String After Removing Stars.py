from collections import defaultdict
from string import ascii_lowercase

class Solution(object):
    def clearStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        g = defaultdict(list)  # dictionary to store indices of each character
        n = len(s)
        rem = [False] * n      # list to mark indices to be removed

        for i, c in enumerate(s):
            if c == "*":
                rem[i] = True
                for ch in ascii_lowercase:
                    if g[ch]:
                        rem[g[ch].pop()] = True
                        break
            else:
                g[c].append(i)

        result = []
        for i, c in enumerate(s):
            if not rem[i]:
                result.append(c)
        return ''.join(result)
