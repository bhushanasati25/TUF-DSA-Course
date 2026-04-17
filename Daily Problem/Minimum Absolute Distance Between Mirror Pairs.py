class Solution(object):
    def minMirrorPairDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_i = {}
        min_dist = float('inf')
        
        for j, val in enumerate(nums):
            if val in max_i:
                min_dist = min(min_dist, j - max_i[val])
            
            target = int(str(val)[::-1])
            max_i[target] = j
            
        return min_dist if min_dist != float('inf') else -1