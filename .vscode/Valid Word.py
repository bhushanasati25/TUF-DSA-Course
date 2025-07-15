class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            return False

        vowels = set("aeiouAEIOU")
        hasVowel = False
        hasConsonant = False

        for ch in word:
            if not ch.isalnum():
                return False
            if ch.isalpha():
                if ch in vowels:
                    hasVowel = True
                else:
                    hasConsonant = True

        return hasVowel and hasConsonant
