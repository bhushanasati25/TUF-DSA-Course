class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        best_d2 = -1   # best squared diagonal so far
        best_area = 0

        for w, h in dimensions:
            d2 = w*w + h*h   # compare squared diagonals (no sqrt)
            area = w*h
            if d2 > best_d2 or (d2 == best_d2 and area > best_area):
                best_d2 = d2
                best_area = area

        return best_area
