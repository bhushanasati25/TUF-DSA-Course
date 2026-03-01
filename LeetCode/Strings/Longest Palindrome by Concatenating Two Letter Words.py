"""
🔗 Problem: Longest Palindrome by Concatenating Two Letter Words
📂 Category: Strings
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

📝 Description:
   Find longest palindrome by concatenating two-letter words.
"""

from collections import Counter

class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = Counter(words)
        length = 0
        center_used = False

        for word in count:
            reverse = word[::-1]
            if word != reverse:
                if reverse in count:
                    pair_count = min(count[word], count[reverse])
                    length += pair_count * 4
                    count[word] -= pair_count
                    count[reverse] -= pair_count
            else:
                pair_count = count[word] // 2
                length += pair_count * 4
                count[word] -= pair_count * 2
                if not center_used and count[word] > 0:
                    length += 2
                    center_used = True

        return length
