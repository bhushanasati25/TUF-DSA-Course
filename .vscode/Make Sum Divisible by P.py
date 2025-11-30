class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0

        seen = {0: -1}    
        pref = 0
        n = len(nums)
        ans = n

        for i, x in enumerate(nums):
            pref = (pref + x) % p
            want = (pref - target) % p
            if want in seen:
                ans = min(ans, i - seen[want])
            seen[pref] = i

        return ans if ans < n else -1
