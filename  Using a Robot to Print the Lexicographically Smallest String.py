from collections import Counter

class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = Counter(s)   
        stack = []         
        result = []        
        smallest = 'a'     

        for c in s:
            cnt[c] -= 1
            while smallest <= 'z' and cnt[smallest] == 0:
                smallest = chr(ord(smallest) + 1)
            stack.append(c)
            while stack and stack[-1] <= smallest:
                result.append(stack.pop())

        while stack:
            result.append(stack.pop())

        return ''.join(result)
