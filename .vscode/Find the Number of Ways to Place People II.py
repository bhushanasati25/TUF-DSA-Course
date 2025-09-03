class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Sort by x ascending; for ties, y descending
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        ans = 0

        for i in range(n):
            yi = points[i][1]
            maxY = float('-inf')  # best (highest) y so far among y <= yi
            for j in range(i + 1, n):
                yj = points[j][1]
                if yj <= yi and yj > maxY:
                    ans += 1
                    maxY = yj
        return ans
