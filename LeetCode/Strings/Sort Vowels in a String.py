"""
🔗 Problem: Sort Vowels in a String
📂 Category: Strings
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/sort-vowels-in-a-string/

📝 Description:
   Sort vowels in a string while keeping consonants in place.
"""

class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')              
        vlist = [ch for ch in s if ch in vowels]
        vlist.sort()
    
        res = []
        idx = 0
        for ch in s:
            if ch in vowels:
                res.append(vlist[idx])
                idx += 1
            else:
                res.append(ch)
        
        return ''.join(res)
