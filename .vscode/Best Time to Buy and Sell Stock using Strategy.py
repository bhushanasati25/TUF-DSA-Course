class Solution(object):
    def maxProfit(self, prices, strategy, k):
        """
        :type prices: List[int]
        :type strategy: List[int]
        :type k: int
        :rtype: int
        """
        n = len(prices)
        half_k = k // 2
        
        base_profit = 0
        for p, s in zip(prices, strategy):
            base_profit += p * s
            
        current_mod_profit = sum(prices[half_k:k])
        
        current_orig_profit = 0
        for i in range(k):
            current_orig_profit += prices[i] * strategy[i]
            
        current_gain = current_mod_profit - current_orig_profit
        
        max_gain = max(0, current_gain)
        
        for i in range(1, n - k + 1):
            leaving_idx = i - 1
            middle_idx = (i - 1) + half_k
            entering_idx = i + k - 1
            
            current_gain += prices[leaving_idx] * strategy[leaving_idx]
            current_gain -= prices[middle_idx]
            current_gain += prices[entering_idx] - (prices[entering_idx] * strategy[entering_idx])
            
            max_gain = max(max_gain, current_gain)
            
        return base_profit + max_gain