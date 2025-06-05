class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        parent = list(range(26))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return
            if ra < rb:
                parent[rb] = ra
            else:
                parent[ra] = rb

        for ch1, ch2 in zip(s1, s2):
            u = ord(ch1) - ord('a')
            v = ord(ch2) - ord('a')
            union(u, v)

        result_chars = []
        for c in baseStr:
            idx = ord(c) - ord('a')
            root_idx = find(idx)
            result_chars.append(chr(root_idx + ord('a')))

        return "".join(result_chars)
