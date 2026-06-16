class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for char in s:
            if char.isalpha():
                res.append(char)
            elif char == '*':
                if res:
                    res.pop()
            elif char == '#':
                res.extend(res[:])
            elif char == '%':
                res.reverse()
                
        return "".join(res)