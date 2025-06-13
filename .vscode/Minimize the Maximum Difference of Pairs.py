class Solution(object):
    def minimizeMax(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        nums.sort()

        def can_form_pairs(max_diff):
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i+1] - nums[i] <= max_diff:
                    count += 1
                    i += 2  # skip the next element as it's paired
                else:
                    i += 1  # try next possible pair
            return count >= p

        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if can_form_pairs(mid):
                high = mid
            else:
                low = mid + 1

        return low
