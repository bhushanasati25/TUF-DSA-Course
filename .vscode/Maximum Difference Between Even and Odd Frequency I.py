from collections import Counter

class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = Counter(s)
        
        odd_freqs = []
        even_freqs = []
        
        for char_freq in freq.values():
            if char_freq % 2 == 1:
                odd_freqs.append(char_freq)
            else:
                even_freqs.append(char_freq)
                
        max_odd_freq = 0
        if odd_freqs: # Constraint: s contains at least one odd frequency char
            max_odd_freq = max(odd_freqs)
            
        min_even_freq = float('inf')
        if even_freqs: # Constraint: s contains at least one even frequency char
            min_even_freq = min(even_freqs)
            
        return max_odd_freq - min_even_freq