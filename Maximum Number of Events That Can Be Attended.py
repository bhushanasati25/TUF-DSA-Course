import heapq

class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        # Sort events based on their start day
        events.sort()
        event_count = 0
        min_heap = []
        i = 0
        n = len(events)
        day = 1
        
        # Iterate until no more events or heap is empty
        while i < n or min_heap:
            # Add events starting today
            while i < n and events[i][0] == day:
                heapq.heappush(min_heap, events[i][1])
                i += 1

            # Remove events that already ended
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            # Attend one event (with the earliest end day)
            if min_heap:
                heapq.heappop(min_heap)
                event_count += 1

            day += 1

        return event_count
