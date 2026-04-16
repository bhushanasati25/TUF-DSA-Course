class Solution(object):
    def solveQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        indices_map = defaultdict(list)
        
        for i, num in enumerate(nums):
            indices_map[num].append(i)
            
        min_dist = [-1] * n
        
        for indices in indices_map.values():
            k = len(indices)
            if k > 1:
                for j in range(k):
                    left_idx = indices[(j - 1) % k]
                    right_idx = indices[(j + 1) % k]
                    
                    dist_to_left = (indices[j] - left_idx + n) % n
                    dist_to_right = (right_idx - indices[j] + n) % n
                    
                    min_dist[indices[j]] = min(dist_to_left, dist_to_right)
                    
        return [min_dist[q] for q in queries]