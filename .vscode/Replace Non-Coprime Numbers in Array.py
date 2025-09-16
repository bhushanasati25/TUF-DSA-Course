from fractions import gcd   

class Solution(object):
    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        st = []
        for x in nums:
            while st:
                g = gcd(st[-1], x)
                if g == 1:
                    break
                x = (st[-1] // g) * x  # lcm
                st.pop()
            st.append(x)
        return st
