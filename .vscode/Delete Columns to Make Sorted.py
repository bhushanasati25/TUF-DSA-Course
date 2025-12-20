class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count = 0
        rows = len(strs)
        cols = len(strs[0])
        
        # Iterate through each column index
        for c in range(cols):
            # Iterate through the rows starting from the second row
            for r in range(1, rows):
                # Compare the current character with the one immediately above it
                if strs[r][c] < strs[r-1][c]:
                    # If it's smaller, the column is not sorted; mark for deletion
                    count += 1
                    break
                    
        return count