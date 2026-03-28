class Solution(object):
    def findTheString(self, lcp):
        """
        :type lcp: List[List[int]]
        :rtype: str
        """
        n = len(lcp)
        word = [""] * n
        curr_char = ord('a')
        
        for i in range(n):
            if not word[i]:
                if curr_char > ord('z'):
                    return ""
                
                for j in range(i, n):
                    if not word[j] and lcp[i][j] > 0:
                        word[j] = chr(curr_char)
                        
                curr_char += 1
                
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    expected_lcp = 1 + (lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0)
                else:
                    expected_lcp = 0
                    
                if lcp[i][j] != expected_lcp:
                    return ""
                    
        return "".join(word)