class Solution(object):
    def maxPower(self, stations, r, k):
        """
        :type stations: List[int]
        :type r: int
        :type k: int
        :rtype: int
        """
        n = len(stations)

        # Prefix sum to get base power at each city in O(1)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stations[i]

        base = [0] * n
        for i in range(n):
            L = max(0, i - r)
            R = min(n - 1, i + r)
            base[i] = pref[R + 1] - pref[L]

        def can(target):
            # Greedy check using a difference array over *cities* for added power
            used = 0
            add_diff = [0] * (n + 1)  # effect over cities; add_diff[x] contributes starting at city x
            running = 0               # current accumulated added power at city i

            for i in range(n):
                running += add_diff[i]
                curr = base[i] + running
                if curr < target:
                    need = target - curr
                    used += need
                    if used > k:
                        return False
                    # Place 'need' stations at position pos = min(i + r, n - 1)
                    # Their effect on cities is [i, i + 2r], so we add to range [i, end]
                    running += need
                    end = i + 2 * r + 1
                    if end <= n:
                        add_diff[end] -= need
            return True

        lo, hi = 0, sum(stations) + k
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
