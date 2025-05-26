from collections import deque, defaultdict

class Solution(object):
    def largestPathValue(self, colors, edges):
        n = len(colors)
        graph = defaultdict(list)
        in_degree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1

        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        
        dp = [[0] * 26 for _ in range(n)]  
        
        result = 0
        processed_nodes = 0
        
        while queue:
            node = queue.popleft()
            processed_nodes += 1
            color_index = ord(colors[node]) - ord('a')
            dp[node][color_index] += 1  
            result = max(result, dp[node][color_index])  
            
            for neighbor in graph[node]:
                for c in range(26):
                    dp[neighbor][c] = max(dp[neighbor][c], dp[node][c])  
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if processed_nodes < n:
            return -1
        
        return result
