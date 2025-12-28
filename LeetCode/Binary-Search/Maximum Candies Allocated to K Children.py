class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        if sum(candies) < k:
            return 0

        left, right = 1, max(candies)
        result = 0

        # Helper function to check feasibility
        def is_possible(x):
            count = sum(candy // x for candy in candies)
            return count >= k

        while left <= right:
            mid = (left + right) // 2
            if is_possible(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result
