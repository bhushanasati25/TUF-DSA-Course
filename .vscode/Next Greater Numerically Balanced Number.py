class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_balanced(x):
            cnt = [0] * 10
            while x:
                x, d = divmod(x, 10)
                if d == 0:              
                    return False
                cnt[d] += 1
                if cnt[d] > d:            
                    return False
            for d in range(1, 10):
                if cnt[d] and cnt[d] != d: 
                    return False
            return True

        n += 1
        while not is_balanced(n):
            n += 1
        return n
