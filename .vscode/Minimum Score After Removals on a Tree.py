class Solution(object):
    def minimumScore(self, nums, edges):
        from collections import defaultdict

        n = len(nums)
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        parent = [-1] * n
        xor = nums[:]
        in_time = [0] * n
        out_time = [0] * n
        time = [0]

        def dfs(u, p):
            parent[u] = p
            in_time[u] = time[0]
            time[0] += 1
            for v in tree[u]:
                if v == p:
                    continue
                dfs(v, u)
                xor[u] ^= xor[v]
            out_time[u] = time[0]
            time[0] += 1

        dfs(0, -1)

        def is_ancestor(u, v):
            # True if u is ancestor of v
            return in_time[u] < in_time[v] and out_time[v] < out_time[u]

        res = float('inf')

        for i in range(len(edges)):
            for j in range(i + 1, len(edges)):
                a, b = edges[i]
                c, d = edges[j]

                # ensure a is parent of b
                if parent[b] != a:
                    a, b = b, a
                if parent[d] != c:
                    c, d = d, c

                if is_ancestor(b, d):
                    # b is ancestor of d
                    x = xor[d]
                    y = xor[b] ^ xor[d]
                    z = xor[0] ^ xor[b]
                elif is_ancestor(d, b):
                    # d is ancestor of b
                    x = xor[b]
                    y = xor[d] ^ xor[b]
                    z = xor[0] ^ xor[d]
                else:
                    x = xor[b]
                    y = xor[d]
                    z = xor[0] ^ xor[b] ^ xor[d]

                vals = [x, y, z]
                res = min(res, max(vals) - min(vals))

        return res
