class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            return "0"
        
        mid = 1 << (n - 1)  
        
        if k == mid:
            return "1"
        
        if k < mid:
            return self.findKthBit(n - 1, k)
        
        new_k = (1 << n) - k
        bit = self.findKthBit(n - 1, new_k)
        
        return "1" if bit == "0" else "0"