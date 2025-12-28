class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        for i, ch in enumerate(s):
            last_seen[ch] = i
            min_last_seen = min(last_seen.values())
            count += min_last_seen + 1
        return count
