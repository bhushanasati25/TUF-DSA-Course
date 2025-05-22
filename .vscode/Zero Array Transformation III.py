import heapq

class Solution(object):
    def maxRemoval(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        n, q = len(nums), len(queries)
        queries.sort(key=lambda x: x[0])  

        available = []  
        selected = []   
        used = 0
        qi = 0  

        for i in range(n):
            while qi < q and queries[qi][0] <= i:
                l, r = queries[qi]
                heapq.heappush(available, (-r, r))
                qi += 1

            while selected and selected[0] < i:
                heapq.heappop(selected)

            while len(selected) < nums[i]:
                if not available:
                    return -1
                _, r = heapq.heappop(available)
                if r < i:
                    return -1
                heapq.heappush(selected, r)
                used += 1

        return q - used  
