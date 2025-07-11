import heapq

class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        # Sort meetings by start time
        meetings.sort()

        # Min-heap for available rooms (room number)
        available = list(range(n))
        heapq.heapify(available)

        # Min-heap for busy rooms: (end_time, room_number)
        busy = []

        # Count of meetings handled by each room
        count = [0] * n

        for start, end in meetings:
            # Free rooms that have finished before current meeting starts
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                # Assign meeting to the available room with smallest index
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                # All rooms are busy, delay meeting to when earliest room is free
                earliest_end_time, room = heapq.heappop(busy)
                duration = end - start
                new_end = earliest_end_time + duration
                heapq.heappush(busy, (new_end, room))

            count[room] += 1

        # Find the room with the highest number of meetings (tie -> smallest index)
        return count.index(max(count))
