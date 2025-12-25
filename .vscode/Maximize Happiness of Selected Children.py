class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort(reverse=True)
        total_happiness = 0
        
        for i in range(k):
            current_val = happiness[i] - i
    
            if current_val <= 0:
                break
            
            total_happiness += current_val
            
        return total_happiness