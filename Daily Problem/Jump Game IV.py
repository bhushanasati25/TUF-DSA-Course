from collections import defaultdict, deque

class Solution(object):
    def minJumps(self, arr):
        n = len(arr)
        if n <= 1:
            return 0
            
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
            
        visited = {0}
        queue = deque([(0, 0)])
        
        while queue:
            node, steps = queue.popleft()
            
            if node == n - 1:
                return steps
                
            for child in graph[arr[node]]:
                if child not in visited:
                    visited.add(child)
                    queue.append((child, steps + 1))
            
            # Python 2 alternative to .clear()
            del graph[arr[node]][:] 
            
            if node + 1 < n and (node + 1) not in visited:
                visited.add(node + 1)
                queue.append((node + 1, steps + 1))
                
            if node - 1 >= 0 and (node - 1) not in visited:
                visited.add(node - 1)
                queue.append((node - 1, steps + 1))
                
        return -1