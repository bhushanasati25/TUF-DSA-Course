class Solution(object):
    def maximumScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        prefix = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                prefix[j][i + 1] = prefix[j][i] + grid[i][j]
                
        prev_pick = [0] * (n + 1)
        prev_skip = [0] * (n + 1)
        
        for j in range(1, n):
            curr_pick = [0] * (n + 1)
            curr_skip = [0] * (n + 1)
            for curr in range(n + 1):
                for prev in range(n + 1):
                    if curr > prev:
                        score = prefix[j - 1][curr] - prefix[j - 1][prev]
                        curr_pick[curr] = max(curr_pick[curr], prev_skip[prev] + score)
                        curr_skip[curr] = max(curr_skip[curr], prev_skip[prev] + score)
                    else:
                        score = prefix[j][prev] - prefix[j][curr]
                        curr_pick[curr] = max(curr_pick[curr], prev_pick[prev] + score)
                        curr_skip[curr] = max(curr_skip[curr], prev_pick[prev])
            prev_pick = curr_pick
            prev_skip = curr_skip
            
        return max(prev_pick)