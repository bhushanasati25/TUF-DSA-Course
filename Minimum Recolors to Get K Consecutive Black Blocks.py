class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        # Count the number of 'W' in the first window of size k
        white_count = blocks[:k].count('W')
        min_recolors = white_count

        # Sliding window: move the window one step at a time
        for i in range(k, len(blocks)):
            # Include new character
            if blocks[i] == 'W':
                white_count += 1
            # Remove old character
            if blocks[i - k] == 'W':
                white_count -= 1

            # Update minimum recolors needed
            min_recolors = min(min_recolors, white_count)

        return min_recolors
