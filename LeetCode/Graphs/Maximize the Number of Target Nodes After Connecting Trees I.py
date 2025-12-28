import sys
sys.setrecursionlimit(10000)

class Solution:
    def maxTargetNodes(self, edges1, edges2, k):
        def build_graph(edges):
            n = len(edges) + 1
            g = [[] for _ in range(n)]
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)
            return g

        def dfs(graph, u, parent, depth):
            if depth < 0:
                return 0
            cnt = 1
            for v in graph[u]:
                if v != parent:
                    cnt += dfs(graph, v, u, depth - 1)
            return cnt

        g1 = build_graph(edges1)
        g2 = build_graph(edges2)

        best2 = 0
        if k > 0:
            for i in range(len(g2)):
                best2 = max(best2, dfs(g2, i, -1, k - 1))

        ans = []
        for i in range(len(g1)):
            ans.append(dfs(g1, i, -1, k) + best2)
        return ans
