from collections import Counter

class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)               
        max_freq = max(freq.values())         
        return sum(v for v in freq.values() if v == max_freq)
