class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftSum = 0
        rightSum = sum(nums)
        ans = []
        
        for num in nums:
            rightSum -= num
        
            ans.append(abs(leftSum - rightSum))
            leftSum += num
            
        return ans