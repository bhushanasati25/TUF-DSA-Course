class Solution(object):
    def kthCharacter(self, k, operations):
        """
        :type k: int
        :type operations: List[int]
        :rtype: str
        """
        import math
        import string

        # Number of operations needed to reach at least length k
        op_count = 0
        total_length = 1  # start with "a"
        while total_length < k:
            total_length *= 2
            op_count += 1

        # Track how many +1 alphabet shifts are applied
        shifts = 0
        
        # Walk backwards through relevant operations
        for i in range(op_count - 1, -1, -1):
            half = 1 << i  # 2^i
            if k > half:
                k -= half
                shifts += operations[i]

        # Return the final character after shifting 'a'
        return string.ascii_lowercase[(ord('a') - ord('a') + shifts) % 26]
