import collections

class DSU(object):
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

class Solution(object):
    def minOperations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        zeros = s.count('0')
        
        if zeros == 0:
            return 0
            
        dsu = [DSU(n + 5), DSU(n + 5)]
        
        p = zeros % 2
        dsu[p].parent[zeros] = dsu[p].find(zeros + 2)
        
        queue = collections.deque([zeros])
        steps = 0
        
        while queue:
            steps += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                
                min_x = max(0, k - (n - curr))
                max_x = min(curr, k)
                
                min_next = curr + k - 2 * max_x
                max_next = curr + k - 2 * min_x
                
                p_next = min_next % 2
                nxt = dsu[p_next].find(min_next)
                
                while nxt <= max_next:
                    if nxt == 0:
                        return steps
                    
                    queue.append(nxt)
                    dsu[p_next].parent[nxt] = dsu[p_next].find(nxt + 2)
                    nxt = dsu[p_next].find(nxt)
                    
        return -1