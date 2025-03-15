class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def can_rob(mid):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= mid:
                    count += 1
                    i += 1  # Skip the next house (non-adjacent selection)
                i += 1
            return count >= k

        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            if can_rob(mid):
                right = mid  # Reduce the max value for a valid `k` selection
            else:
                left = mid + 1  # Increase search range to find a valid selection
                
        return left  # The minimum possible maximum value for `k` robbed houses
