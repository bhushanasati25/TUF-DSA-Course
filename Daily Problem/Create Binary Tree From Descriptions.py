# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        nodes = {}
        children = set()
        
        for p, c, is_left in descriptions:
            if p not in nodes:
                nodes[p] = TreeNode(p)
            if c not in nodes:
                nodes[c] = TreeNode(c)
                
            if is_left:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]
                
            children.add(c)
            
        for node_val, node in nodes.items():
            if node_val not in children:
                return node
                
        return None