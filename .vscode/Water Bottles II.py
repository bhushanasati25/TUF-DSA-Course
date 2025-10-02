class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        full = numBottles
        empty = 0
        k = numExchange
        drank = 0

        while True:
            # Drink all full bottles
            if full > 0:
                drank += full
                empty += full
                full = 0

            # Try one exchange if possible
            if empty >= k:
                empty -= k
                k += 1
                full += 1
            else:
                break

        return drank
