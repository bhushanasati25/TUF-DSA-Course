"""
🔗 Problem: Remove Sub-Folders from the Filesystem
📂 Category: Strings
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

📝 Description:
   Remove all sub-folders that are children of another folder.
"""

class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort()
        result = [folder[0]]
        
        for path in folder[1:]:
            if not path.startswith(result[-1] + '/'):
                result.append(path)
        
        return result
