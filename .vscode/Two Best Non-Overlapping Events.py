import heapq

class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort()
        pq = []
        
        max_val = 0
        ans = 0    
        
        for start, end, value in events:
            while pq and pq[0][0] < start:
                _, v = heapq.heappop(pq)
                max_val = max(max_val, v)
            ans = max(ans, max_val + value)
        
            heapq.heappush(pq, (end, value))
            
        return ans