class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        vowels = set('aeiou')

        def devowel(s):
            # Replace vowels with '*', so “leet” -> "l**t"
            return ''.join('*' if ch in vowels else ch for ch in s)

        # 1. Exact matches
        exact = set(wordlist)

        # 2. Case-insensitive map: lowercase -> first occurrence
        lower_map = {}
        # 3. Vowel-error map: devoweled(lower) -> first occurrence
        vowel_map = {}

        for w in wordlist:
            lw = w.lower()
            if lw not in lower_map:
                lower_map[lw] = w
            dv = devowel(lw)
            if dv not in vowel_map:
                vowel_map[dv] = w

        result = []
        for q in queries:
            if q in exact:
                result.append(q)
                continue
            lq = q.lower()
            if lq in lower_map:
                result.append(lower_map[lq])
                continue
            dvq = devowel(lq)
            result.append(vowel_map.get(dvq, ""))
        return result
