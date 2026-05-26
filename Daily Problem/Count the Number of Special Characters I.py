class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        char_set = set(word)
        count = 0
    
        for lower, upper in zip(string.ascii_lowercase, string.ascii_uppercase):
            if lower in char_set and upper in char_set:
                count += 1
                
        return count