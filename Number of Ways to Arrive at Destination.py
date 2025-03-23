import heapq

class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        
        We want the number of shortest paths from node 0 to node n-1.
        
        Approach:
        1. Build an adjacency list for the graph.
        2. Use Dijkstra's algorithm to find shortest distances from 0 to every node.
        3. Maintain a 'ways' array where ways[i] = number of ways to reach node i 
           via a shortest path.
        4. If we find a strictly shorter path to a node v via u, we update dist[v] 
           and set ways[v] = ways[u].
        5. If we find another path with the same distance, we add ways[u] to ways[v].
        6. The result is ways[n-1] % (10^9 + 7).
        """
        
        MOD = 10**9 + 7
        
        # 1. Build adjacency list: graph[node] = [(neighbor, travel_time), ...]
        graph = [[] for _ in range(n)]
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))
        
        # 2. Dijkstra’s setup
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        
        # Min-heap holds pairs (current_distance, node)
        heap = [(0, 0)]
        
        while heap:
            cur_dist, u = heapq.heappop(heap)
            
            # If this distance isn't the latest known shortest distance, skip
            if cur_dist > dist[u]:
                continue
            
            # Explore neighbors
            for v, t in graph[u]:
                new_dist = cur_dist + t
                # Found a strictly better path
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    ways[v] = ways[u]
                    heapq.heappush(heap, (new_dist, v))
                # Found another equally good shortest path
                elif new_dist == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD
        
        return ways[n - 1] % MOD
