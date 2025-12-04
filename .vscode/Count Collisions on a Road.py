class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        s = directions
        n = len(s)

        i = 0
        while i < n and s[i] == 'L':
            i += 1

        j = n - 1
        while j >= 0 and s[j] == 'R':
            j -= 1

        collisions = 0
        for k in range(i, j + 1):
            if s[k] != 'S':
                collisions += 1

        return collisions
