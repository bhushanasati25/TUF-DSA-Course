from fractions import Fraction

class Solution(object):
    def judgePoint24(self, cards):
        """
        :type cards: List[int]
        :rtype: bool
        """
        nums = [Fraction(x, 1) for x in cards]
        return self._dfs(nums)

    def _dfs(self, arr):
        if len(arr) == 1:
            return arr[0] == 24

        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                a, b = arr[i], arr[j]
                rest = [arr[k] for k in range(n) if k != i and k != j]

                # Use a set to avoid duplicate results for commutative ops
                results = set()
                results.add(a + b)
                results.add(a * b)
                results.add(a - b)
                results.add(b - a)
                if b != 0:
                    results.add(a / b)
                if a != 0:
                    results.add(b / a)

                for val in results:
                    if self._dfs(rest + [val]):
                        return True
        return False
