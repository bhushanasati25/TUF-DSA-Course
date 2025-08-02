from collections import Counter

class Solution(object):
    def minCost(self, basket1, basket2):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """
        # Step 1: Count all fruit occurrences across both baskets
        total = Counter(basket1 + basket2)

        # If any fruit occurs odd number of times, impossible to rearrange
        for count in total.values():
            if count % 2 != 0:
                return -1

        # Step 2: Find surplus in basket1 and basket2
        c1 = Counter(basket1)
        c2 = Counter(basket2)

        surplus1 = []
        surplus2 = []

        for fruit in total:
            diff = c1[fruit] - c2[fruit]
            if diff > 0:
                surplus1.extend([fruit] * (diff // 2))
            elif diff < 0:
                surplus2.extend([fruit] * ((-diff) // 2))

        # Sort the surpluses: one ascending, one descending
        surplus1.sort()
        surplus2.sort(reverse=True)

        # Step 3: Use greedy swapping
        min_value = min(total.keys())
        total_cost = 0

        for a, b in zip(surplus1, surplus2):
            total_cost += min(min(a, b), 2 * min_value)

        return total_cost
