class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        dx = abs(x - z)
        dy = abs(y - z)
        
        if dx == dy:
            return 0
        return 1 if dx < dy else 2
