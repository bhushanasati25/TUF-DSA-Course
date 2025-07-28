class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_or = 0
        for num in nums:
            max_or |= num  # Find the maximum OR of the whole array

        self.count = 0  # To count the number of subsets that achieve max_or

        def dfs(index, current_or):
            if index == len(nums):
                if current_or == max_or:
                    self.count += 1
                return
            # Exclude current number
            dfs(index + 1, current_or)
            # Include current number
            dfs(index + 1, current_or | nums[index])

        dfs(0, 0)
        return self.count
