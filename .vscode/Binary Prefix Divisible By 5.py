class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        res = []
        val = 0

        for b in nums:
            val = ((val << 1) + b) % 5
            res.append(val == 0)

        return res
