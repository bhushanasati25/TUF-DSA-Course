class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = max(nums)
        if len(nums) != n + 1:
            return False
            
        count = Counter(nums)
        for i in range(1, n):
            if count[i] != 1:
                return False
                
        return count[n] == 2