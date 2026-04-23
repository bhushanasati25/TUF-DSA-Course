class Solution(object):
    def distance(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        
        groups = defaultdict(list)
        for i, val in enumerate(nums):
            groups[val].append(i)
            
        n = len(nums)
        res = [0] * n
        
        for indices in groups.values():
            m = len(indices)
            
            if m == 1:
                continue
                
            left_sum = 0
            right_sum = sum(indices)
            
            for i in range(m):
                idx = indices[i]
                
                right_sum -= idx
                
                left_dist = (i * idx) - left_sum
                right_dist = right_sum - ((m - 1 - i) * idx)
                
                res[idx] = left_dist + right_dist
                
                left_sum += idx
                
        return res