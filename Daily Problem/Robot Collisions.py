class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        """
        :type positions: List[int]
        :type healths: List[int]
        :type directions: str
        :rtype: List[int]
        """
        robots = sorted(zip(positions, healths, directions, range(len(positions))))
        stack = []
        
        for p, h, d, i in robots:
            if d == 'R':
                stack.append([p, h, d, i])
            else:
                while stack and stack[-1][2] == 'R' and h > 0:
                    if stack[-1][1] < h:
                        stack.pop()
                        h -= 1
                    elif stack[-1][1] > h:
                        stack[-1][1] -= 1
                        h = 0
                    else:
                        stack.pop()
                        h = 0
                
                if h > 0:
                    stack.append([p, h, d, i])
                    
        stack.sort(key=lambda x: x[3])
        return [robot[1] for robot in stack]