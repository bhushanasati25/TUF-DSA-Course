class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        def get_min_finish(start1, dur1, start2, dur2):
            min_first = min(s + d for s, d in zip(start1, dur1))
            return min(max(min_first, s) + d for s, d in zip(start2, dur2))
        
        return min(
            get_min_finish(landStartTime, landDuration, waterStartTime, waterDuration),
            get_min_finish(waterStartTime, waterDuration, landStartTime, landDuration)
        )