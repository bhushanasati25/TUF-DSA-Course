class Solution(object):
    def maxDistinctElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        last = float('-inf')
        count = 0

        for num in nums:
            place = max(last + 1, num - k)
            if place <= num + k:
                count += 1
                last = place

        return count
