import heapq

class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        
        next_node = list(range(1, n + 1))
        next_node[-1] = -1 
        
        prev_node = list(range(-1, n - 1))
        
        vals = list(nums)
        ver = [0] * n
        
        inversion_count = 0
        pq = []
        
        for i in range(n - 1):
            if vals[i] > vals[i+1]:
                inversion_count += 1

            heapq.heappush(pq, (vals[i] + vals[i+1], i, i+1, ver[i], ver[i+1]))
            
        if inversion_count == 0:
            return 0
            
        ops = 0
        
        while inversion_count > 0:
            if not pq:
                break
            
            current_sum, u, v, v_u, v_v = heapq.heappop(pq)
            
            if ver[u] != v_u or ver[v] != v_v or next_node[u] != v:
                continue
            
            ops += 1
            
            left = prev_node[u]
            right = next_node[v]
            
            if left != -1 and vals[left] > vals[u]:
                inversion_count -= 1
            if vals[u] > vals[v]:
                inversion_count -= 1
            if right != -1 and vals[v] > vals[right]:
                inversion_count -= 1
            
            vals[u] = vals[u] + vals[v]
            
            next_node[u] = right
            if right != -1:
                prev_node[right] = u

            ver[u] += 1
            ver[v] += 1 
            
            if left != -1:
                if vals[left] > vals[u]:
                    inversion_count += 1

                heapq.heappush(pq, (vals[left] + vals[u], left, u, ver[left], ver[u]))
            
            if right != -1:
                if vals[u] > vals[right]:
                    inversion_count += 1
                heapq.heappush(pq, (vals[u] + vals[right], u, right, ver[u], ver[right]))
                
        return ops