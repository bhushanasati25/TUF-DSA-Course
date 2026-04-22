class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        res = []
        
        for q in queries:
            for d in dictionary:
                diff = 0
                
                for a, b in zip(q, d):
                    if a != b:
                        diff += 1
                    if diff > 2:
                        break
                
                if diff <= 2:
                    res.append(q)
                    break
        
        return res