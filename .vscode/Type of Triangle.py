class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Step 1: Sort the side lengths
        nums.sort()
        
        # Step 2: Check for a valid triangle using the triangle inequality
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        
        # Step 3: Determine the type of triangle
        if nums[0] == nums[2]:
            return "equilateral"
        elif nums[0] == nums[1] or nums[1] == nums[2]:
            return "isosceles"
        else:
            return "scalene"
