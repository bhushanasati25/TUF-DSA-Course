class Solution(object):
    def assignEdgeWeights(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        if not edges:
            return 0
            
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        max_depth = 0
        queue = deque([(1, 0)])
        visited = [False] * (n + 1)
        visited[1] = True
        
        while queue:
            curr, depth = queue.popleft()
            max_depth = depth
            
            for neighbor in adj[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, depth + 1))
                    
        if max_depth == 0:
            return 0
            
        return pow(2, max_depth - 1, 10**9 + 7)