class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        
        counts = defaultdict(int)
        
        # Accumulate sums from nums1
        for id_val, val in nums1:
            counts[id_val] += val
        
        # Accumulate sums from nums2
        for id_val, val in nums2:
            counts[id_val] += val
        
        # Convert to list of [id, total_val] and sort by 'id'
        merged = sorted([[id_val, total] for id_val, total in counts.items()])
        
        return merged
