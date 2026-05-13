class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        n = len(nums)
        delta = [0] * (2 * limit + 2)
        
        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]
            
            min_val = min(a, b)
            max_val = max(a, b)
            
            delta[min_val + 1] -= 1
            delta[a + b] -= 1
            delta[a + b + 1] += 1
            delta[max_val + limit + 1] += 1
            
        current_moves = n 
        min_moves = n
        
        for target in range(2, 2 * limit + 1):
            current_moves += delta[target]
            if current_moves < min_moves:
                min_moves = current_moves
                
        return min_moves