class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter

        total_distinct = len(set(nums))  # Total number of distinct elements in the array
        count_map = Counter()
        left = 0
        result = 0

        for right in range(len(nums)):
            count_map[nums[right]] += 1

            # Shrink the window while it still contains all distinct elements
            while len(count_map) == total_distinct:
                result += len(nums) - right  # Count all subarrays starting from `left` to end
                count_map[nums[left]] -= 1
                if count_map[nums[left]] == 0:
                    del count_map[nums[left]]
                left += 1

        return result
