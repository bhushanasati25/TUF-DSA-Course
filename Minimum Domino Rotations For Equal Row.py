class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """

        def check(x):
            rotations_a = rotations_b = 0
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return float('inf') 
                elif tops[i] != x:
                    rotations_a += 1  
                elif bottoms[i] != x:
                    rotations_b += 1  
            return min(rotations_a, rotations_b)

        candidates = [tops[0], bottoms[0]]
        min_rotations = min(check(candidates[0]), check(candidates[1]))

        return -1 if min_rotations == float('inf') else min_rotations
