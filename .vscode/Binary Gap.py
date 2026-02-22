class Solution(object):
    def binaryGap(self, n):
        b = bin(n)[2:]
        prev = None
        ans = 0

        for i, bit in enumerate(b):
            if bit == '1':
                if prev is not None:
                    ans = max(ans, i - prev)
                prev = i

        return ans