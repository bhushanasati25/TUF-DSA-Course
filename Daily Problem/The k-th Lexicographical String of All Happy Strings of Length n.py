class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.result = ""
        self.count = 0
        
        def backtrack(current):
            if self.result:
                return
            
            if len(current) == n:
                self.count += 1
                if self.count == k:
                    self.result = current
                return
            
            for char in ['a', 'b', 'c']:
                if not current or current[-1] != char:
                    backtrack(current + char)
        
        backtrack("")
        return self.result