"""
🔗 Problem: Find X-Sum of All K-Long Subarrays I
📂 Category: Sliding-Window
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/

📝 Description:
   Sum of top-x frequent elements in each k-length subarray.
"""

from collections import defaultdict

class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(nums)
        if k <= 0 or k > n:
            return []

        freq = defaultdict(int)

        for i in range(k):
            freq[nums[i]] += 1

        def x_sum_current():
            items = sorted(freq.items(), key=lambda it: (-it[1], -it[0]))
            total = 0
            for val, cnt in items[:x]:
                total += val * cnt
            return total

        ans = [x_sum_current()]

        for i in range(k, n):
            out_v = nums[i - k]
            freq[out_v] -= 1
            if freq[out_v] == 0:
                del freq[out_v]

            in_v = nums[i]
            freq[in_v] += 1

            ans.append(x_sum_current())

        return ans
