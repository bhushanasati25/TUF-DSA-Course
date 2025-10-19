class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        # local gcd (works on LeetCode Py2/Py3)
        def _gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        n = len(s)
        digits = list(map(int, s))
        steps = 10 // _gcd(a, 10)   # additions cycle length per parity

        best = None
        seen_rot = set()
        rot = 0  # cumulative right-rotation amount

        for _ in range(n):
            if rot in seen_rot:
                break
            seen_rot.add(rot)

            # rotate right by 'rot' == left by n-rot
            L = n - rot
            t = digits[L:] + digits[:L]

            def build(k_odd, k_even):
                u = t[:]  # copy
                # add to odd indices
                for i in range(1, n, 2):
                    u[i] = (u[i] + k_odd * a) % 10
                # if b is odd, parity mixes, so evens can be adjusted too
                if b % 2 == 1:
                    for i in range(0, n, 2):
                        u[i] = (u[i] + k_even * a) % 10
                return ''.join(str(d) for d in u)

            if b % 2 == 0:
                for k_odd in range(steps):
                    cand = build(k_odd, 0)
                    if best is None or cand < best:
                        best = cand
            else:
                for k_odd in range(steps):
                    for k_even in range(steps):
                        cand = build(k_odd, k_even)
                        if best is None or cand < best:
                            best = cand

            rot = (rot + b) % n

        return best
