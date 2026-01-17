class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        """
        :type bottomLeft: List[List[int]]
        :type topRight: List[List[int]]
        :rtype: int
        """
        n = len(bottomLeft)
        max_area = 0

        for i in range(n):
            x1, y1 = bottomLeft[i]
            x2, y2 = topRight[i]

            for j in range(i + 1, n):
                x3, y3 = bottomLeft[j]
                x4, y4 = topRight[j]

                width = min(x2, x4) - max(x1, x3)
                height = min(y2, y4) - max(y1, y3)

                if width > 0 and height > 0:
                    side = min(width, height)
                    max_area = max(max_area, side * side)

        return max_area
