class Solution(object):
    def maxStability(self, n, edges, k):
        mandatory = []
        optional = []
        candidates = set()
        
        for u, v, s, must in edges:
            candidates.add(s)
            if must == 1:
                mandatory.append((u, v, s))
            else:
                optional.append((u, v, s))
                candidates.add(s * 2)
                
        sorted_cands = sorted(list(candidates))
        
        def check(x):
            parent = list(range(n))
            
            def find(i):
                curr = i
                while parent[curr] != curr:
                    curr = parent[curr]
                p = i
                while p != curr:
                    nxt = parent[p]
                    parent[p] = curr
                    p = nxt
                return curr

            edges_count = 0
            
            for u, v, s in mandatory:
                if s < x: return False
                root_u, root_v = find(u), find(v)
                if root_u == root_v: return False
                parent[root_u] = root_v
                edges_count += 1
                
            free_optional = []
            upgrade_optional = []
            for u, v, s in optional:
                if s >= x:
                    free_optional.append((u, v))
                elif s * 2 >= x:
                    upgrade_optional.append((u, v))
                    
            for u, v in free_optional:
                root_u, root_v = find(u), find(v)
                if root_u != root_v:
                    parent[root_u] = root_v
                    edges_count += 1
                    
            upgrades_used = 0
            for u, v in upgrade_optional:
                if upgrades_used == k: break
                root_u, root_v = find(u), find(v)
                if root_u != root_v:
                    parent[root_u] = root_v
                    edges_count += 1
                    upgrades_used += 1
                    
            return edges_count == n - 1

        ans = -1
        left, right = 0, len(sorted_cands) - 1
        while left <= right:
            mid = (left + right) // 2
            if check(sorted_cands[mid]):
                ans = sorted_cands[mid]
                left = mid + 1
            else:
                right = mid - 1
                
        return ans