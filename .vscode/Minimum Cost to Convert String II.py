class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        nodes = list(set(original) | set(changed))
        str_to_id = {s: i for i, s in enumerate(nodes)}
        m = len(nodes)
        
        dist = [[float('inf')] * m for _ in range(m)]
        for i in range(m): dist[i][i] = 0
        for u_s, v_s, c in zip(original, changed, cost):
            u, v = str_to_id[u_s], str_to_id[v_s]
            dist[u][v] = min(dist[u][v], c)
            
        for k in range(m):
            for i in range(m):
                if dist[i][k] == float('inf'): continue
                for j in range(m):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        trie = {}
        for s in nodes:
            curr = trie
            for char in s:
                curr = curr.setdefault(char, {})
            curr['_id'] = str_to_id[s]
            
        n = len(source)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(n):
            if dp[i] == float('inf'): continue
            
            if source[i] == target[i]:
                dp[i+1] = min(dp[i+1], dp[i])
            
            curr_s, curr_t = trie, trie
            for j in range(i, n):
                if source[j] not in curr_s or target[j] not in curr_t:
                    break
                curr_s = curr_s[source[j]]
                curr_t = curr_t[target[j]]

                if '_id' in curr_s and '_id' in curr_t:
                    u, v = curr_s['_id'], curr_t['_id']
                    if dist[u][v] != float('inf'):
                        dp[j+1] = min(dp[j+1], dp[i] + dist[u][v])
                        
        return int(dp[n]) if dp[n] != float('inf') else -1