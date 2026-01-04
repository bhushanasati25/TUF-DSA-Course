class Solution(object):
    def sumFourDivisors(self, nums):
        total_sum = 0
        
        for n in nums:
            divisors = [1, n]
            
            i = 2
            while i * i <= n:
                if n % i == 0:
                    divisors.append(i)
                    if i != n // i:
                        divisors.append(n // i)
                    
                    if len(divisors) > 4:
                        break
                i += 1
            
            if len(divisors) == 4:
                total_sum += sum(divisors)
        
        return total_sum
