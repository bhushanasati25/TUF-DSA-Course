"""
📝 Question:
Implement a Binary Search Tree (BST) with the following operations:
  1. Insert a value (maintain BST property: left < root < right)
  2. Search for a value
  3. Delete a node (handle all 3 cases: leaf, one child, two children)
  4. Inorder traversal (gives sorted output for BST)
"""

# Binary Search Tree (BST) - Insert, Search, Delete
# BST Property: left < root < right

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, val):
    if not root:
        return Node(val)
    if val < root.data:
        root.left = insert(root.left, val)
    elif val > root.data:
        root.right = insert(root.right, val)
    return root


def search(root, val):
    if not root:
        return False
    if root.data == val:
        return True
    if val < root.data:
        return search(root.left, val)
    return search(root.right, val)


def find_min(root):
    while root.left:
        root = root.left
    return root


def delete_node(root, val):
    if not root:
        return None

    if val < root.data:
        root.left = delete_node(root.left, val)
    elif val > root.data:
        root.right = delete_node(root.right, val)
    else:
        # Node found — 3 cases
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        # Two children: replace with inorder successor
        successor = find_min(root.right)
        root.data = successor.data
        root.right = delete_node(root.right, successor.data)
    return root


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.data] + inorder(root.right)


if __name__ == "__main__":
    root = None
    for val in [50, 30, 70, 20, 40, 60, 80]:
        root = insert(root, val)

    print(f"BST Inorder: {inorder(root)}")
    print(f"Search 40: {'Found' if search(root, 40) else 'Not Found'}")
    print(f"Search 25: {'Found' if search(root, 25) else 'Not Found'}")

    root = delete_node(root, 30)
    print(f"After deleting 30: {inorder(root)}")
