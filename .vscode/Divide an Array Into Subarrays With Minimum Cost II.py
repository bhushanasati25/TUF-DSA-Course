import heapq

class Solution(object):
    def minimumCost(self, nums, k, dist):
        k -= 1 
        n = len(nums)
        
        L, R = [], []
        L_sum = 0
        in_L = [False] * n
        
        def push_to_L(val, idx):
            heapq.heappush(L, (-val, idx))
            in_L[idx] = True
            return val

        def push_to_R(val, idx):
            heapq.heappush(R, (val, idx))
            in_L[idx] = False

        for i in range(1, min(n, dist + 2)):
            L_sum += push_to_L(nums[i], i)
        
        while len(L) > k:
            val, idx = heapq.heappop(L)
            L_sum -= -val
            push_to_R(-val, idx)
            
        min_cost = L_sum
        
        for i in range(dist + 2, n):
            out_idx = i - (dist + 1)
            in_val = nums[i]
            
            if in_L[out_idx]:
                L_sum -= nums[out_idx]
                cnt_L = k - 1
            else:
                cnt_L = k
            
            push_to_R(in_val, i)
            while L and L[0][1] <= out_idx: heapq.heappop(L)
            while R and R[0][1] <= out_idx: heapq.heappop(R)
            
            if cnt_L < k:
                val, idx = heapq.heappop(R)
                L_sum += push_to_L(val, idx)
                
            while L and L[0][1] <= out_idx: heapq.heappop(L)
            while R and R[0][1] <= out_idx: heapq.heappop(R)
                
            if L and R and -L[0][0] > R[0][0]:
                val_l, idx_l = heapq.heappop(L)
                val_r, idx_r = heapq.heappop(R)
                
                L_sum -= -val_l 
                push_to_R(-val_l, idx_l)
                
                L_sum += val_r  
                push_to_L(val_r, idx_r)
                
            min_cost = min(min_cost, L_sum)
            
        return nums[0] + min_cost