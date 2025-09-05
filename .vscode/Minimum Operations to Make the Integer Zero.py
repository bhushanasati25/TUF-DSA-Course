class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        # Try k operations, where 0 <= k <= 60 is plenty for 64-bit ranges
        for k in range(61):
            x = num1 - k * num2
            if x < 0:
                # If num2 > 0, x will only get smaller as k grows → stop early
                if num2 > 0:
                    break
                # If num2 <= 0, larger k might make x >= 0 later → continue
                continue

            # Minimum #powers-of-two needed is popcount(x); maximum is x (all 1s)
            pop = bin(x).count("1")  # works on all Python versions
            if pop <= k <= x:
                return k

        return -1
