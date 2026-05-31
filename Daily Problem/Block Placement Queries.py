from sortedcontainers import SortedList

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (2 * n)
        
    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        i //= 2
        while i > 0:
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])
            i //= 2
            
    def query(self, l, r):
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l % 2 == 1:
                res = max(res, self.tree[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                res = max(res, self.tree[r])
            l //= 2
            r //= 2
        return res

class Solution(object):
    def getResults(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        limit = min(50000, 3 * len(queries)) + 5
        seg = SegmentTree(limit)
        obstacles = SortedList([0, limit - 1])
        seg.update(limit - 1, limit - 1)
        
        ans = []
        for q in queries:
            if q[0] == 1:
                x = q[1]
                idx = obstacles.bisect_right(x)
                nxt = obstacles[idx]
                prev = obstacles[idx - 1]
                
                obstacles.add(x)
                seg.update(x, x - prev)
                seg.update(nxt, nxt - x)
            else:
                x, sz = q[1], q[2]
                idx = obstacles.bisect_right(x)
                prev = obstacles[idx - 1]
                
                max_gap_before = seg.query(0, prev + 1)
                max_gap = max(max_gap_before, x - prev)
                ans.append(max_gap >= sz)
                
        return ans