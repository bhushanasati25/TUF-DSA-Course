class Solution(object):
    def smallestSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        last = [-1] * 32  # Track last seen index for each bit
        ans = [1] * n

        for i in range(n - 1, -1, -1):
            length = 1
            for bit in range(32):
                if nums[i] >> bit & 1:
                    last[bit] = i
                elif last[bit] != -1:
                    length = max(length, last[bit] - i + 1)
            ans[i] = length

        return ans
