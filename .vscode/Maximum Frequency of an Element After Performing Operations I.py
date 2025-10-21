from collections import Counter, defaultdict

class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        """
        :type nums: List[int]
        :type k: int
        :type numOperations: int
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        n = len(nums)
        cnt = Counter(nums)
        uniq = sorted(cnt.keys())

        ans1 = 1
        l = 0
        r = 0 
        for y in uniq:
            upper = y + k
            lower = y - k
            while r < n and nums[r] <= upper:
                r += 1
            while l < n and nums[l] < lower:
                l += 1
            R_y = r - l          
            E_y = cnt[y]     
            best_y = min(R_y, E_y + numOperations)
            if best_y > ans1:
                ans1 = best_y

        events = defaultdict(int)
        for x in nums:
            start = x - k
            end = x + k
            events[start] += 1
            events[end + 1] -= 1   

        run = 0
        M = 0
        for pos in sorted(events):
            run += events[pos]
            if run > M:
                M = run

        ans2 = min(M, numOperations)

        return max(ans1, ans2)
