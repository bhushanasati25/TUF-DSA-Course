class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import Counter

        freq = Counter(arr)
        lucky = -1

        for num in freq:
            if num == freq[num]:
                lucky = max(lucky, num)

        return lucky
