class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_even = 0
        count_odd = 0
        even_len = 0
        odd_len = 0

        for x in nums:
            if x % 2 == 0:
                count_even += 1
                even_len = max(even_len, odd_len + 1)
            else:
                count_odd += 1
                odd_len = max(odd_len, even_len + 1)

        candidates = [even_len, odd_len]
        if count_even >= 2:
            candidates.append(count_even)
        if count_odd >= 2:
            candidates.append(count_odd)

        return max(candidates)
