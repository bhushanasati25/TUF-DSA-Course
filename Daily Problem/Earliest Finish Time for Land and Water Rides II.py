class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        n, m = len(landStartTime), len(waterStartTime)
        
        min_EL = min(landStartTime[i] + landDuration[i] for i in range(n))
        min_EW = min(waterStartTime[j] + waterDuration[j] for j in range(m))
        
        ans_land_first = min(max(min_EL, waterStartTime[j]) + waterDuration[j] for j in range(m))
        ans_water_first = min(max(min_EW, landStartTime[i]) + landDuration[i] for i in range(n))
        
        return min(ans_land_first, ans_water_first)