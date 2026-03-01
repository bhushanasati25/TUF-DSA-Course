"""
🔗 Problem: Sum of Root To Leaf Binary Numbers
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

📝 Description:
   Sum all root-to-leaf binary numbers in a binary tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, curr):
            if not node:
                return 0
            
            curr = curr * 2 + node.val
            
            if not node.left and not node.right:
                return curr

            return dfs(node.left, curr) + dfs(node.right, curr)
        
        return dfs(root, 0)