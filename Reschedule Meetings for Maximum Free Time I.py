class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        """
        :type eventTime: int
        :type k: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        n = len(startTime)
        # Build the gaps array: size n+1
        gaps = [0] * (n + 1)
        # Free time before first meeting
        gaps[0] = startTime[0]
        # Free times between meetings
        for i in range(1, n):
            gaps[i] = startTime[i] - endTime[i - 1]
        # Free time after last meeting
        gaps[n] = eventTime - endTime[-1]

        # Determine window size: can cover at most all gaps
        window_size = min(k + 1, n + 1)
        # Sum of the first window
        current_sum = sum(gaps[:window_size])
        max_sum = current_sum

        # Slide the window over the gaps array
        for i in range(window_size, n + 1):
            current_sum += gaps[i] - gaps[i - window_size]
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum
