class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        robot.sort()
        factory.sort()
        
        memo = {}
        
        def dp(i, j):
            if i == len(robot):
                return 0
            if j == len(factory):
                return float('inf')
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            res = dp(i, j + 1)
            
            limit = factory[j][1]
            pos = factory[j][0]
            cost = 0
            
            for k in range(1, limit + 1):
                if i + k - 1 < len(robot):
                    cost += abs(robot[i + k - 1] - pos)
                    res = min(res, cost + dp(i + k, j + 1))
                else:
                    break
                    
            memo[(i, j)] = res
            return res
            
        return dp(0, 0)