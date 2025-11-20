class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[1], -x[0]))

        a = -10**18
        b = -10**18
        ans = 0

        for l, r in intervals:
            if l > b:
                ans += 2
                a, b = r - 1, r
            elif l > a:
                ans += 1
                a, b = b, r
            else:
                pass

        return ans
