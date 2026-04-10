from collections import defaultdict, deque

class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        indices = defaultdict(list)
    
        for i, x in enumerate(nums):
            indices[x].append(i)
        
        best = float('inf')

        for idx_list in indices.values():
            if len(idx_list) >= 3:
                for i in range(len(idx_list) - 2):
                    dist = 2 * (idx_list[i + 2] - idx_list[i])
                    best = min(best, dist)

        return -1 if best == float('inf') else best
        