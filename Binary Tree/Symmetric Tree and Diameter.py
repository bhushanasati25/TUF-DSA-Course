# Symmetric Tree Check & Diameter of Binary Tree
# Time: O(n) | Space: O(h)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_mirror(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    return (left.data == right.data and
            is_mirror(left.left, right.right) and
            is_mirror(left.right, right.left))


def is_symmetric(root):
    if not root:
        return True
    return is_mirror(root.left, root.right)


def diameter_helper(root, result):
    if not root:
        return 0
    left_h = diameter_helper(root.left, result)
    right_h = diameter_helper(root.right, result)
    result[0] = max(result[0], left_h + right_h)
    return 1 + max(left_h, right_h)


def diameter(root):
    result = [0]
    diameter_helper(root, result)
    return result[0]


if __name__ == "__main__":
    # Symmetric tree:      1
    #                    /   \
    #                   2     2
    #                  / \   / \
    #                 3   4 4   3
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(3)

    print(f"Is Symmetric: {'Yes' if is_symmetric(root) else 'No'}")
    print(f"Diameter: {diameter(root)}")
