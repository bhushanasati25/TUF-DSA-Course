class Solution:
    def intersectionArray(self, nums1, nums2):
        return sorted(set(nums1).intersection(set(nums2)))
        