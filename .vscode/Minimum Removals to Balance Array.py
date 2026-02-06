class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums.sort()
        n = len(nums)

        def upperBound(arr, limit):
            low, high = 0, n - 1
            ans = n 

            while low <= high:
                mid = (low + high) // 2

                if arr[mid] > limit:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1

            return ans

        max_keep = 0

        for i in range(n):
            limit = nums[i] * k
            j = upperBound(nums, limit)
            max_keep = max(max_keep, j - i)

        return n - max_keep
