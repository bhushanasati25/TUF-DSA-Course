class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        
        Returns the number of days without any meetings scheduled.
        """
        if not meetings:
            return days
        
        clipped = []
        for start, end in meetings:
            s = max(start, 1)
            e = min(end, days)
            if s <= e:
                clipped.append([s, e])
        
        if not clipped:
            return days
        
        clipped.sort(key=lambda x: x[0])
    
        merged = []
        for interval in clipped:
            if not merged:
                merged.append(interval)
            else:
                last = merged[-1]
                if interval[0] <= last[1] + 1: 
                    last[1] = max(last[1], interval[1])
                else:
                    merged.append(interval)
        
        meeting_days = 0
        for s, e in merged:
            meeting_days += (e - s + 1)
        
        return days - meeting_days


