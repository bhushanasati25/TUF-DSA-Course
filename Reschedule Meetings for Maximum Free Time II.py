class Solution(object):
    def maxFreeTime(self, eventTime, startTime, endTime):
        """
        :type eventTime: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        n = len(startTime)

        # Step 1: Compute gaps between meetings
        gaps = [0] * (n + 1)
        gaps[0] = startTime[0]
        for i in range(1, n):
            gaps[i] = startTime[i] - endTime[i - 1]
        gaps[n] = eventTime - endTime[-1]

        # Step 2: Precompute prefix and suffix maximums of gaps
        maxLeft = [0] * (n + 1)
        maxLeft[0] = gaps[0]
        for i in range(1, n + 1):
            maxLeft[i] = max(maxLeft[i - 1], gaps[i])

        maxRight = [0] * (n + 2)
        maxRight[n] = gaps[n]
        for i in range(n - 1, -1, -1):
            maxRight[i] = max(maxRight[i + 1], gaps[i])

        # Step 3: Try removing each meeting and merging its adjacent gaps
        max_free_time = 0
        for i in range(n):
            duration = endTime[i] - startTime[i]
            adjacent_gap = gaps[i] + gaps[i + 1]

            # Try moving the meeting somewhere else
            best_outside = 0
            if i - 1 >= 0:
                best_outside = max(best_outside, maxLeft[i - 1])
            if i + 2 <= n:
                best_outside = max(best_outside, maxRight[i + 2])

            if duration <= best_outside:
                max_free_time = max(max_free_time, adjacent_gap + duration)
            else:
                max_free_time = max(max_free_time, adjacent_gap)

        return max_free_time
