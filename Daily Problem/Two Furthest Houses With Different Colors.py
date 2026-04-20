class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)

        max_dist_from_start = 0

        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                max_dist_from_start = i - 0
                break

        
        max_dist_from_end = 0

        for i in range(n):
            if colors[i] != colors[n - 1]:
                max_dist_from_end = (n - 1) - i 
                break

        
        return max(max_dist_from_start, max_dist_from_end)