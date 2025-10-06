from heapq import heappush, heappop

class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        # Min-heap of (time_required, r, c)
        heap = [(grid[0][0], 0, 0)]
        seen = [[False]*n for _ in range(n)]
        dirs = ((1,0), (-1,0), (0,1), (0,-1))

        while heap:
            t, r, c = heappop(heap)
            if seen[r][c]:
                continue
            seen[r][c] = True
            if r == n - 1 and c == n - 1:
                return t
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not seen[nr][nc]:
                    heappush(heap, (max(t, grid[nr][nc]), nr, nc))
