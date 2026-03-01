# Binary Tree - Basic Operations
# Create, Insert, Inorder/Preorder/Postorder Traversal, Height, Count Nodes

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_level_order(root, val):
    """Level-order insertion (builds a complete binary tree)."""
    new_node = Node(val)
    if not root:
        return new_node

    queue = deque([root])
    while queue:
        node = queue.popleft()
        if not node.left:
            node.left = new_node
            return root
        else:
            queue.append(node.left)
        if not node.right:
            node.right = new_node
            return root
        else:
            queue.append(node.right)
    return root


def inorder(root):
    """Left -> Root -> Right"""
    if not root:
        return []
    return inorder(root.left) + [root.data] + inorder(root.right)


def preorder(root):
    """Root -> Left -> Right"""
    if not root:
        return []
    return [root.data] + preorder(root.left) + preorder(root.right)


def postorder(root):
    """Left -> Right -> Root"""
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.data]


def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))


def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


if __name__ == "__main__":
    root = None
    for val in [1, 2, 3, 4, 5, 6, 7]:
        root = insert_level_order(root, val)

    print(f"Inorder:   {inorder(root)}")
    print(f"Preorder:  {preorder(root)}")
    print(f"Postorder: {postorder(root)}")
    print(f"Height: {height(root)}")
    print(f"Total Nodes: {count_nodes(root)}")
