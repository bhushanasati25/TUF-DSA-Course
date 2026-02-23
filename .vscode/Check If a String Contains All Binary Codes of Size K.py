class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        
        n = len(s)

        if n - k + 1 < (1 << k):
            return False

        seen = set()

        for i in range(n - k + 1):
            substring = s[i:i+k]
            seen.add(substring)

            if len(seen) == (1 << k):
                return True

        return False