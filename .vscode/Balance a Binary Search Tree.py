# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sorted_vals.append(node.val)
            inorder(node.right)
        
        def buildBalanced(left, right):

            if left > right:
                return None
            
            mid = (left + right) // 2
            node = TreeNode(sorted_vals[mid])
            node.left = buildBalanced(left, mid - 1)
            node.right = buildBalanced(mid + 1, right)
            
            return node
        
        sorted_vals = []
        inorder(root)
    
        return buildBalanced(0, len(sorted_vals) - 1)