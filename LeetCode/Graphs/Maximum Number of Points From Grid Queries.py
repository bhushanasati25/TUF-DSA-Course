import heapq

class Solution(object):
    def maxPoints(self, grid, queries):
        """
        :type grid: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        query_with_index = sorted([(val, idx) for idx, val in enumerate(queries)])
        res = [0] * len(queries)
        min_heap = [(grid[0][0], 0, 0)]
        visited[0][0] = True
        count = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        heapq.heapify(min_heap)

        i = 0  
        while i < len(query_with_index):
            q_val, q_idx = query_with_index[i]
            while min_heap and min_heap[0][0] < q_val:
                val, x, y = heapq.heappop(min_heap)
                count += 1

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        heapq.heappush(min_heap, (grid[nx][ny], nx, ny))
                        visited[nx][ny] = True

            while i < len(query_with_index) and query_with_index[i][0] == q_val:
                res[query_with_index[i][1]] = count
                i += 1

        return res
