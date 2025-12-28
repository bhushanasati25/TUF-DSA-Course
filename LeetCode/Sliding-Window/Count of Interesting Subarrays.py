from collections import defaultdict

class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        """
        :type nums: List[int]
        :type modulo: int
        :type k: int
        :rtype: int
        """
        count_map = defaultdict(int)
        count_map[0] = 1 
        prefix_mod_sum = 0
        result = 0

        for num in nums:
            is_interesting = 1 if num % modulo == k else 0
            prefix_mod_sum = (prefix_mod_sum + is_interesting) % modulo
            target_mod = (prefix_mod_sum - k + modulo) % modulo
            result += count_map[target_mod]
            count_map[prefix_mod_sum] += 1

        return result
