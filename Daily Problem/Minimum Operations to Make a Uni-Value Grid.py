class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
    
        flat = [num for row in grid for num in row]
        
        rem = flat[0] % x
        for num in flat:
            if num % x != rem:
                return -1

        flat.sort()
        median = flat[len(flat) // 2]

        return sum(abs(num - median) // x for num in flat)
