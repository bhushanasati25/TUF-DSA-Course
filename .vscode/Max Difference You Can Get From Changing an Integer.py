class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = list(str(num))
        
        max_s = s[:]
        for digit in max_s:
            if digit != '9':
                target = digit
                max_s = ['9' if c == target else c for c in max_s]
                break
        max_num = int(''.join(max_s))
        
        min_s = s[:]
        if min_s[0] != '1':
            target = min_s[0]
            min_s = ['1' if c == target else c for c in min_s]
        else:
            for i in range(1, len(min_s)):
                if min_s[i] not in ('0', '1'):
                    target = min_s[i]
                    min_s = ['0' if c == target else c for c in min_s]
                    break
        min_num = int(''.join(min_s))
        
        return max_num - min_num
