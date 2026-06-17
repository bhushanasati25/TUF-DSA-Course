class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        lengths = []
        curr_len = 0
        
        for char in s:
            if char == '*':
                curr_len = max(0, curr_len - 1)
            elif char == '#':
                curr_len *= 2
            elif char == '%':
                pass 
            else:
                curr_len += 1
            lengths.append(curr_len)
            
        if k >= lengths[-1]:
            return '.'
            
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            prev_len = lengths[i-1] if i > 0 else 0
            
            if char == '*':
                pass 
            elif char == '#':
                if k >= prev_len:
                    k -= prev_len
            elif char == '%':
                k = lengths[i] - 1 - k
            else:
                if k == lengths[i] - 1:
                    return char
        
        return '.'