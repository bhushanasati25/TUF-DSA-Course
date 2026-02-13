class Solution(object):
    def longestBalanced(self, s):
        n = len(s)
        ans = 0
        
        cnt = 0
        for i in range(n):
            if i > 0 and s[i] == s[i-1]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)
            
        for u, v in [('a', 'b'), ('b', 'c'), ('c', 'a')]:
            mp = {0: -1}
            diff = 0
            for i, char in enumerate(s):
                if char == u:
                    diff += 1
                elif char == v:
                    diff -= 1
                else:
                    mp = {0: i}
                    diff = 0
                    continue
                
                if diff in mp:
                    ans = max(ans, i - mp[diff])
                else:
                    mp[diff] = i

        mp = {(0, 0): -1}
        ca = cb = cc = 0
        for i, char in enumerate(s):
            if char == 'a': ca += 1
            elif char == 'b': cb += 1
            elif char == 'c': cc += 1
            
            key = (ca - cb, cb - cc)
            
            if key in mp:
                ans = max(ans, i - mp[key])
            else:
                mp[key] = i
                
        return ans