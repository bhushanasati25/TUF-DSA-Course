class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        count = 1  

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1  

            if count < 3:
                result.append(s[i])
            elif count == 2:
                if i == 1:
                    result.append(s[i - 1])
                result.append(s[i])

        return s[0] + ''.join(result) if s else ''
