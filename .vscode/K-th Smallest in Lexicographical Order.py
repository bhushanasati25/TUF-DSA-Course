class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        curr = 1
        k -= 1  
        while k > 0:
            # Calculate the number of steps (count of numbers) in the subtree
            # rooted at 'curr'
            steps = 0
            first_num_in_level = curr
            last_num_in_level = curr + 1

            while first_num_in_level <= n:
                steps += min(n + 1, last_num_in_level) - first_num_in_level
                first_num_in_level *= 10
                last_num_in_level *= 10
            
            if k >= steps:
                # The k-th number is not in the current subtree, move to the next sibling
                curr += 1
                k -= steps
            else:
                # The k-th number is in the current subtree, go deeper
                curr *= 10
                k -= 1 # Decrement k because we are 'stepping into' the current number
        
        return curr