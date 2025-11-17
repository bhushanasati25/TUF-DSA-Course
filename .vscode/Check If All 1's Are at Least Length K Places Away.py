class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prev_one = -1   
        
        for i, val in enumerate(nums):
            if val == 1:
                if prev_one != -1 and i - prev_one - 1 < k:
                    return False
                prev_one = i  
                
        return True
