class Solution(object):
    def maxDistance(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def calc(a, b):
            curr = 0
            cnt = 0
            best = 0
            for c in s:
                if c == a or c == b:
                    curr += 1
                elif cnt < k:
                    curr += 1
                    cnt += 1
                else:
                    curr -= 1
                best = max(best, curr)
            return best

        return max(
            calc('N', 'E'),
            calc('N', 'W'),
            calc('S', 'E'),
            calc('S', 'W')
        )
