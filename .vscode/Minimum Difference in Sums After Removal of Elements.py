import heapq

class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) // 3
        
        prefix_min_sums = [0] * (3 * n)
        max_heap = [] 
        current_sum = 0
        
        for i in range(2 * n):
            current_sum += nums[i]
            heapq.heappush(max_heap, -nums[i])
            
            if len(max_heap) > n:
                largest_val = -heapq.heappop(max_heap)
                current_sum -= largest_val
            
            if len(max_heap) == n:
                prefix_min_sums[i] = current_sum

        suffix_max_sums = [0] * (3 * n)
        min_heap = []
        current_sum = 0
    
        for i in range(3 * n - 1, n - 1, -1):
            current_sum += nums[i]
            heapq.heappush(min_heap, nums[i])
            
            if len(min_heap) > n:
                smallest_val = heapq.heappop(min_heap)
                current_sum -= smallest_val
            
            if len(min_heap) == n:
                suffix_max_sums[i] = current_sum
                
        min_diff = float('inf')
        
        for i in range(n - 1, 2 * n):
            diff = prefix_min_sums[i] - suffix_max_sums[i + 1]
            min_diff = min(min_diff, diff)
            
        return min_diff