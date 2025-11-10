class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        stack = [0]  
        for x in nums:
            while stack and stack[-1] > x:
                stack.pop()
            if not stack or stack[-1] < x:
                ans += 1
                stack.append(x)
        return ans
