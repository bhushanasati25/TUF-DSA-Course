"""
📝 Question:
Given the root of a binary tree, return its level order traversal.
Level order traversal visits nodes level by level from left to right (BFS).

Example:
  Input:  Tree [1, 2, 3, 4, 5, 6, 7]
  Output: [[1], [2, 3], [4, 5, 6, 7]]
"""

# Level Order Traversal (BFS) of Binary Tree
# Time: O(n) | Space: O(n)

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    levels = level_order(root)
    print("Level Order Traversal:")
    for i, level in enumerate(levels):
        print(f"  Level {i}: {level}")
