from collections import Counter

class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1 = nums1
        self.nums2 = nums2
        self.count2 = Counter(nums2)

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        old_val = self.nums2[index]
        new_val = old_val + val
        self.count2[old_val] -= 1
        if self.count2[old_val] == 0:
            del self.count2[old_val]
        self.nums2[index] = new_val
        self.count2[new_val] += 1

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        result = 0
        for num in self.nums1:
            complement = tot - num
            result += self.count2.get(complement, 0)
        return result
