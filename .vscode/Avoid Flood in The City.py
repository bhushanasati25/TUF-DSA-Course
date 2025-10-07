class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        import bisect

        n = len(rains)
        ans = [-1] * n          # default for rain days; will set to lake id on chosen dry days
        last_fill = {}          # lake -> last day it was filled
        dry_days = []           # sorted list of indices where rains[i] == 0

        for i, lake in enumerate(rains):
            if lake == 0:
                # Save dry day for later; placeholder 1 (may be overwritten)
                bisect.insort(dry_days, i)
                ans[i] = 1
            else:
                # It's raining on lake
                if lake in last_fill:
                    # Need a dry day strictly after last_fill[lake]
                    j = bisect.bisect_right(dry_days, last_fill[lake])
                    if j == len(dry_days):
                        return []  # impossible to prevent a flood
                    dry_idx = dry_days.pop(j)
                    ans[dry_idx] = lake  # dry this lake on that dry day
                last_fill[lake] = i
                ans[i] = -1  # raining day

        return ans
