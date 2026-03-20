class Solution(object):
    def minAbsDiff(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                nums = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        nums.append(grid[x][y])
                
                nums.sort()
                min_diff = float('inf')
                
                for t in range(1, len(nums)):
                    if nums[t] != nums[t - 1]:
                        diff = nums[t] - nums[t - 1]
                        if diff < min_diff:
                            min_diff = diff
                
                if min_diff != float('inf'):
                    ans[i][j] = min_diff
                    
        return ans