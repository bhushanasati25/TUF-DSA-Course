class Solution(object):
    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        def dist(a, b):
            if a == 26:
                return 0
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)
            
        dp = {26: 0}
        
        for i in range(len(word)):
            c = ord(word[i]) - 65
            p = ord(word[i-1]) - 65 if i > 0 else 26
            
            new_dp = {}
            for other_finger, cost in dp.items():
                new_dp[other_finger] = min(new_dp.get(other_finger, float('inf')), cost + dist(p, c))
                new_dp[p] = min(new_dp.get(p, float('inf')), cost + dist(other_finger, c))
                
            dp = new_dp
            
        return min(dp.values())