class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        """
        :type nums: List[int]
        :type k: int
        :type edges: List[List[int]]
        :rtype: int
        """
        total = 0
        diffs = []

        for num in nums:
            original = num
            toggled = num ^ k
            total += original
            diffs.append(toggled - original)

        diffs.sort(reverse=True)

        for i in range(0, len(diffs) - 1, 2):
            gain = diffs[i] + diffs[i + 1]
            if gain > 0:
                total += gain
            else:
                break

        return total
