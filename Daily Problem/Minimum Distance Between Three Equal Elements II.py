from collections import deque
class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_two = {}
        best = float('inf')

        for i, x in enumerate(nums):
            dq = last_two.get(x)
            if dq is None:
                dq = deque(maxlen=2)
                last_two[x] = dq

            if len(dq) == 2:
                best = min(best, 2 * (i - dq[0]))

            dq.append(i)

        return -1 if best == float('inf') else best
            
        
        
        