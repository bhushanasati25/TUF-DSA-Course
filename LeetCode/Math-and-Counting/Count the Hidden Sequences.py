class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        min_sum = max_sum = curr = 0
        for diff in differences:
            curr += diff
            min_sum = min(min_sum, curr)
            max_sum = max(max_sum, curr)
        
        return max(0, (upper - max_sum) - (lower - min_sum) + 1)
