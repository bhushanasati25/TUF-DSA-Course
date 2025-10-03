import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0

        visited = [[False] * n for _ in range(m)]
        heap = []  # (height, r, c)

        # Push all border cells into the min-heap
        for r in range(m):
            for c in (0, n - 1):
                heapq.heappush(heap, (heightMap[r][c], r, c))
                visited[r][c] = True
        for c in range(n):
            for r in (0, m - 1):
                if not visited[r][c]:
                    heapq.heappush(heap, (heightMap[r][c], r, c))
                    visited[r][c] = True

        trapped = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            h, r, c = heapq.heappop(heap)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    nh = heightMap[nr][nc]
                    if nh < h:
                        trapped += h - nh
                        heapq.heappush(heap, (h, nr, nc))  # water raises neighbor to boundary height
                    else:
                        heapq.heappush(heap, (nh, nr, nc))

        return trapped
