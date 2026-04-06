class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_idx = 0 
        x, y = 0, 0
        max_dist_sq = 0
        obstacle_set = set(map(tuple, obstacles))
        
        for cmd in commands:
            if cmd == -1:
                direction_idx = (direction_idx + 1) % 4
            elif cmd == -2:
                direction_idx = (direction_idx - 1) % 4
            else:
                for _ in range(cmd):
                    next_x = x + directions[direction_idx][0]
                    next_y = y + directions[direction_idx][1]
                    
                    if (next_x, next_y) in obstacle_set:
                        break
                    
                    x, y = next_x, next_y
                    max_dist_sq = max(max_dist_sq, x*x + y*y)
                    
        return max_dist_sq