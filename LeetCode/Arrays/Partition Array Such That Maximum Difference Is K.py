"""
🔗 Problem: Partition Array Such That Maximum Difference Is K
📂 Category: Arrays
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

📝 Description:
   Partition array into minimum subsequences with max diff ≤ k.
"""

class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Sort the array to group close elements together
        nums.sort()
        
        count = 1  # At least one group is needed
        start = nums[0]  # Start of the current group

        for num in nums:
            if num - start > k:
                # Start a new group
                count += 1
                start = num  # Reset the start of new group

        return count
