class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        complete_count = 0

        def dfs(start):
            stack = [start]
            visited[start] = True
            nodes_in_comp = []
            edge_count = 0  

            while stack:
                node = stack.pop()
                nodes_in_comp.append(node)
                for neighbor in graph[node]:
                    edge_count += 1
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
            
            return nodes_in_comp, edge_count // 2

        for i in range(n):
            if not visited[i]:
                comp_nodes, e = dfs(i)
                k = len(comp_nodes)
                if e == k * (k - 1) // 2:
                    complete_count += 1

        return complete_count
