class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type values: List[int]
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0

        # build adjacency list
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        order = []
        stack = [0]
        parent[0] = -2  

        while stack:
            u = stack.pop()
            order.append(u)
            for v in graph[u]:
                if parent[v] == -1:
                    parent[v] = u
                    stack.append(v)

        subtree_mod = [0] * n
        ans = 0
        for u in reversed(order):
            total_mod = values[u] % k
            for v in graph[u]:
                if parent[v] == u:  # v is a child of u
                    total_mod = (total_mod + subtree_mod[v]) % k
            subtree_mod[u] = total_mod
            if subtree_mod[u] == 0:
                ans += 1

        return ans
