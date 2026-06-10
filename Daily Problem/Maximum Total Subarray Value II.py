class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if not n or not k: return 0
        
        LOG = n.bit_length()
        st_max = [list(nums)]
        st_min = [list(nums)]
        
        for j in range(1, LOG):
            prev_max = st_max[-1]
            prev_min = st_min[-1]
            step = 1 << (j - 1)
            
            cur_max = [max(prev_max[i], prev_max[i + step]) for i in range(n - (1 << j) + 1)]
            cur_min = [min(prev_min[i], prev_min[i + step]) for i in range(n - (1 << j) + 1)]
            
            st_max.append(cur_max)
            st_min.append(cur_min)
            
        def get_val(l, r):
            j = (r - l + 1).bit_length() - 1
            return max(st_max[j][l], st_max[j][r - (1 << j) + 1]) - min(st_min[j][l], st_min[j][r - (1 << j) + 1])

        heap = [(-get_val(0, n - 1), 0, n - 1)]
        visited = {(0, n - 1)}
        total = 0
        
        for _ in range(k):
            val, l, r = heapq.heappop(heap)
            total -= val
            if l < r:
                if (l + 1, r) not in visited:
                    visited.add((l + 1, r))
                    heapq.heappush(heap, (-get_val(l + 1, r), l + 1, r))
                if (l, r - 1) not in visited:
                    visited.add((l, r - 1))
                    heapq.heappush(heap, (-get_val(l, r - 1), l, r - 1))
                    
        return total