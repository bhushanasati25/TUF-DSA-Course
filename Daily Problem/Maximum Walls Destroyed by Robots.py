from bisect import bisect_left, bisect_right

class Solution(object):
    def maxWalls(self, robots, distance, walls):
        """
        :type robots: List[int]
        :type distance: List[int]
        :type walls: List[int]
        :rtype: int
        """
        n = len(robots)
        if n == 0:
            return 0

        paired = sorted(zip(robots, distance))

        r = [p for p, _ in paired]
        d = [q for _, q in paired]

        walls.sort()
        m = len(walls)

        def count_incl(lo, hi):
            if lo > hi:
                return 0

            return bisect_right(walls, hi) - bisect_left(walls, lo)

        at_robot = set(walls)
        base = sum(1 for x in r if x in at_robot)

        L = [0]*(n -1)
        Rg = [0]*(n-1)
        U = [0]*(n-1)

        for i in range(n-1):
            left_robot, right_robot = r[i], r[i + 1]
            total_between = count_incl(left_robot + 1, right_robot - 1)

            right_limit = min(left_robot + d[i], right_robot - 1)
            L[i] = count_incl(left_robot + 1, right_limit)

            left_limit = max(right_robot - d[i+1], left_robot + 1)
            Rg[i] = count_incl(left_limit, right_robot-1)

            ov_lo = max(left_robot + 1, right_robot - d[i+1])
            ov_hi = min(right_robot-1, left_robot + d[i])
            overlap = count_incl(ov_lo, ov_hi)
            U[i] = min(total_between, L[i] + Rg[i] - overlap)

        leftmost_gain = count_incl(r[0] - d[0], r[0] - 1)
        rightmost_gain = count_incl(r[-1]+1, r[-1]+d[-1])

        dpL = leftmost_gain
        dpR = 0

        for i in range(1, n):
            newL = max(
                dpR + U[i -1],
                dpL + Rg[i - 1],
                dpR + 0,
                dpL + 0
            )

            newR = max(
                dpR + L[i -1],
                dpL + 0
            )

            dpL, dpR = newL, newR

        best_gap_cover = max(dpL, dpR + rightmost_gain)
        return base + best_gap_cover
        