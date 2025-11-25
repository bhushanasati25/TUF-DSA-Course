class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        # If k is divisible by 2 or 5, no repunit can ever be divisible by k
        if k % 2 == 0 or k % 5 == 0:
            return -1

        rem = 0
        
        # At most k iterations because remainders repeat
        for length in range(1, k + 1):
            rem = (rem * 10 + 1) % k
            if rem == 0:
                return length
        
        return -1
