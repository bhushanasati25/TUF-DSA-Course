class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        indexed_nums = list(enumerate(nums))  # (index, value)

        top_k = sorted(indexed_nums, key=lambda x: x[1], reverse=True)[:k]
        top_k_sorted_by_index = sorted(top_k, key=lambda x: x[0])

        return [num for idx, num in top_k_sorted_by_index]
