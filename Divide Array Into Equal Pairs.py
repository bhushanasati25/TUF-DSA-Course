from collections import Counter

class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) % 2 != 0:
            return False
        
        count = Counter(nums)
        for freq in count.values():
            if freq % 2 != 0:
                return False
                
        return True
