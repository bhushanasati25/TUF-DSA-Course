from collections import deque
import heapq

class Solution(object):
    def processQueries(self, c, connections, queries):
        """
        :type c: int
        :type connections: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # 1) Build undirected graph
        g = [[] for _ in range(c + 1)]
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)

        # 2) Find connected components (fixed; stations going offline don't change edges)
        comp = [0] * (c + 1)          # comp[i] = component id (1..k) of node i
        heaps = [None]                # heaps[comp_id] -> min-heap of station ids in that component; index 0 unused
        k = 0

        for start in range(1, c + 1):
            if comp[start] != 0:
                continue
            k += 1
            q = deque([start])
            comp[start] = k
            members = [start]
            while q:
                u = q.popleft()
                for w in g[u]:
                    if comp[w] == 0:
                        comp[w] = k
                        q.append(w)
                        members.append(w)
            # Build a min-heap of all members (all start online)
            h = members[:]
            heapq.heapify(h)
            heaps.append(h)

        # 3) Process queries with lazy deletion via `offline` bitmap
        offline = [False] * (c + 1)
        ans = []

        for t, x in queries:
            if t == 1:
                if not offline[x]:
                    # If x is online, it's the answer immediately
                    ans.append(x)
                else:
                    cid = comp[x]
                    h = heaps[cid]
                    # Pop offline nodes until top is online (or heap empties)
                    while h and offline[h[0]]:
                        heapq.heappop(h)
                    ans.append(h[0] if h else -1)
            else:
                # t == 2: take station x offline
                offline[x] = True

        return ans
