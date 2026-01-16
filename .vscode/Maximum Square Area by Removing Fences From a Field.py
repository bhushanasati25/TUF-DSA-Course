class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        :type m: int
        :type n: int
        :type hFences: List[int]
        :type vFences: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7

        def getDistances(fences, limit):
            fences = fences + [1, limit]
            fences.sort()
            distances = set()
            for i in range(len(fences)):
                for j in range(i):
                    distances.add(fences[i] - fences[j])
            return distances

        h_dist = getDistances(hFences, m)
        v_dist = getDistances(vFences, n)

        common = h_dist & v_dist
        if not common:
            return -1

        max_side = max(common)
        return (max_side * max_side) % MOD
