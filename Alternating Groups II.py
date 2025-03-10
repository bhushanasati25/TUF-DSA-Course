class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        n = len(colors)
        count = 0
        length = 1
        
        # Iterate 2*n - 1 to handle circular array
        for i in range(1, 2 * n):
            if colors[i % n] != colors[(i - 1) % n]:
                length = length + 1 if 'length' in locals() else 2
            else:
                length = 1
            
            if length >= k:
                count += 1 if 'count' in locals() else 1
                
        return count
