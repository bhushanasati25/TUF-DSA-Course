"""
🔗 Problem: Minimum Number of People to Teach
📂 Category: Math-and-Counting
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/minimum-number-of-people-to-teach/

📝 Description:
   Min people to teach a language so all friends can communicate.
"""

class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        m = len(languages)  # number of people
        know = [set()] * (m + 1)  # DON'T keep this; replace properly below
        know = [set()] + [set(langs) for langs in languages]

        to_fix = set()
        for u, v in friendships:
            if know[u].isdisjoint(know[v]):
                to_fix.add(u)
                to_fix.add(v)

        if not to_fix:
            return 0

        freq = [0] * (n + 1)  # freq[lang]
        for person in to_fix:
            for lang in know[person]:
                freq[lang] += 1

        best_already = max(freq)  
        return len(to_fix) - best_already
