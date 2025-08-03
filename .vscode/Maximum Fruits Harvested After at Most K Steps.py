class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        """
        :type fruits: List[List[int]]
        :type startPos: int
        :type k: int
        :rtype: int
        """
        n = len(fruits)
        prefix = [0] * (n + 1)
        positions = [pos for pos, _ in fruits]
        
        for i in range(n):
            prefix[i + 1] = prefix[i] + fruits[i][1]
        
        max_fruits = 0
        i = 0
        
        for j in range(n):
            left = fruits[i][0]
            right = fruits[j][0]
            
            # Cost to travel from startPos to cover [left, right]
            cost = (right - left) + min(abs(startPos - left), abs(startPos - right))
            
            # Shrink window from the left if cost exceeds k
            while i <= j and cost > k:
                i += 1
                if i <= j:
                    left = fruits[i][0]
                    cost = (right - left) + min(abs(startPos - left), abs(startPos - right))
                    
            if i <= j:
                max_fruits = max(max_fruits, prefix[j + 1] - prefix[i])
        
        return max_fruits
