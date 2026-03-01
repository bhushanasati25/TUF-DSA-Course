"""
🔗 Problem: Balanced Binary Tree
📂 Category: Trees
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/balanced-binary-tree/

📝 Description:
   Check if a binary tree is height-balanced.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(node):
            if not node:
                return 0 

            left = dfs(node.left)
            if left == -1:
                return -1  

            right = dfs(node.right)
            if right == -1:
                return -1 

            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return dfs(root) != -1