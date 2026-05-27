class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        last_lower = [-1] * 26
        first_upper = [float('inf')] * 26
        
        for i, char in enumerate(word):
            if char.islower():
                last_lower[ord(char) - ord('a')] = i
            else:
                idx = ord(char) - ord('A')
                if first_upper[idx] == float('inf'):
                    first_upper[idx] = i
                    
        special_count = 0
        for i in range(26):
            if last_lower[i] != -1 and first_upper[i] != float('inf') and last_lower[i] < first_upper[i]:
                special_count += 1
                
        return special_count