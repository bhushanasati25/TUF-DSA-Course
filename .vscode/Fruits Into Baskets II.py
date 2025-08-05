class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n = len(fruits)
        used = [False] * n  # Tracks which baskets have been used
        ans = n  # Start with all fruits unplaced

        for x in fruits:
            for i in range(n):
                if not used[i] and baskets[i] >= x:
                    used[i] = True  # Mark basket as used
                    ans -= 1        # Successfully placed a fruit
                    break           # Move to the next fruit
        return ans
