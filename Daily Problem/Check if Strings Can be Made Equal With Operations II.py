class Solution(object):
    def checkStrings(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        count = [[0]*26 for _ in range(2)] 
        
        for i in range(len(s1)):
            idx = ord(s1[i]) - ord('a')
            count[i % 2][idx] += 1
            
            idx = ord(s2[i]) - ord('a')
            count[i % 2][idx] -= 1
        
        for i in range(2):
            for j in range(26):
                if count[i][j] != 0:
                    return False
        
        return True