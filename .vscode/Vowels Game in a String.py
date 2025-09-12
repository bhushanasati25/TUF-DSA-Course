class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = set("aeiou")
        # Alice wins if there is at least one vowel
        return any(c in vowels for c in s)
