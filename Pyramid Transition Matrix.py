class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        from collections import defaultdict
        
        mp = defaultdict(list)
        for a, b, c in allowed:
            mp[a + b].append(c)
        
        memo = set() 
        
        def dfs(curr):
            if len(curr) == 1:
                return True
            
            if curr in memo:
                return False
            
            for i in range(len(curr) - 1):
                if curr[i:i+2] not in mp:
                    memo.add(curr)
                    return False
            
            def build_next(idx, path, res):
                if idx == len(curr) - 1:
                    res.append(path)
                    return
                pair = curr[idx:idx+2]
                for ch in mp[pair]:
                    build_next(idx + 1, path + ch, res)
            
            next_rows = []
            build_next(0, "", next_rows)
            
            for row in next_rows:
                if dfs(row):
                    return True
            
            memo.add(curr)
            return False
        
        return dfs(bottom)
