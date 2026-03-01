# Find the Middle of a Linked List
# Using slow and fast pointer approach
# Time: O(n) | Space: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    middle = find_middle(head)
    print(f"Middle element: {middle.data}")
