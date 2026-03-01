"""
🔗 Problem: Count Good Numbers
📂 Category: Math-and-Counting
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/count-good-numbers/

📝 Description:
   Count digit strings with even digits at even positions, primes at odd.
"""

class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        def mod_pow(base, exponent):
            result = 1
            base %= MOD
            while exponent > 0:
                if exponent % 2 == 1:
                    result = (result * base) % MOD
                base = (base * base) % MOD
                exponent //= 2
            return result
        
        even_count = (n + 1) // 2  
        odd_count = n // 2         

        return (mod_pow(5, even_count) * mod_pow(4, odd_count)) % MOD
