from itertools import combinations

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def area(a, b, c):
            (x1, y1), (x2, y2), (x3, y3) = a, b, c
            # Shoelace formula
            return 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))

        best = 0.0
        for a, b, c in combinations(points, 3):
            cur = area(a, b, c)
            if cur > best:
                best = cur
        return best
