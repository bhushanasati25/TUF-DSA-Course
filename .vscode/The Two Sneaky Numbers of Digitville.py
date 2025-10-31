class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) - 2          # values are guaranteed in [0, n-1]
        dup = []
        freq = [0] * n
        for x in nums:
            freq[x] += 1
            if freq[x] == 2:
                dup.append(x)
                if len(dup) == 2:
                    break
        dup.sort()
        return dup
