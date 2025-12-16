class Solution(object):
    def maxProfit(self, n, present, future, hierarchy, budget):
        """
        :type n: int
        :type present: List[int]
        :type future: List[int]
        :type hierarchy: List[List[int]]
        :type budget: int
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for u, v in hierarchy:
            adj[u-1].append(v-1)
            
        def merge(dp_acc, dp_child):
            new_dp = [-float('inf')] * (budget + 1)

            for i in range(budget + 1):
                current_max = -float('inf')
                for j in range(i + 1):
                    val = dp_acc[i - j] + dp_child[j]
                    if val > current_max:
                        current_max = val
                new_dp[i] = current_max
            return new_dp

        def dfs(u):
            sum_nb = [0] * (budget + 1)
            sum_b = [0] * (budget + 1)
            
            for v in adj[u]:
                child_res_nb, child_res_b = dfs(v)
                sum_nb = merge(sum_nb, child_res_nb)
                sum_b = merge(sum_b, child_res_b)
            
            res_nb = [0] * (budget + 1)
            cost_full = present[u]
            profit_full = future[u] - cost_full
            
            for w in range(budget + 1):
                opt_dont_buy = sum_nb[w]
                
                opt_buy = -float('inf')
                if w >= cost_full:
                    opt_buy = profit_full + sum_b[w - cost_full]
                
                res_nb[w] = max(opt_dont_buy, opt_buy)
        
            res_b = [0] * (budget + 1)
            cost_half = present[u] // 2
            profit_half = future[u] - cost_half
            
            for w in range(budget + 1):
                opt_dont_buy = sum_nb[w]
                opt_buy = -float('inf')
                if w >= cost_half:
                    opt_buy = profit_half + sum_b[w - cost_half]
                
                res_b[w] = max(opt_dont_buy, opt_buy)
                
            return res_nb, res_b

        root_nb, _ = dfs(0)
        return max(0, root_nb[budget])