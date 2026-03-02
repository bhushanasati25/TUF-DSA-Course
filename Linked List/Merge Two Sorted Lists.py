"""
📝 Question:
Given the heads of two sorted linked lists, merge them into one sorted list.
The merged list should be made by splicing together the nodes of the two lists.

Example:
  Input:  1 → 3 → 5, 2 → 4 → 6
  Output: 1 → 2 → 3 → 4 → 5 → 6
"""

# Merge Two Sorted Linked Lists
# Time: O(n + m) | Space: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_two_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2
    return dummy.next


def display(head):
    elements = []
    while head:
        elements.append(str(head.data))
        head = head.next
    print(" -> ".join(elements) + " -> NULL")


if __name__ == "__main__":
    l1 = Node(1)
    l1.next = Node(3)
    l1.next.next = Node(5)

    l2 = Node(2)
    l2.next = Node(4)
    l2.next.next = Node(6)

    print("List 1: ", end="")
    display(l1)
    print("List 2: ", end="")
    display(l2)

    merged = merge_two_lists(l1, l2)
    print("Merged: ", end="")
    display(merged)
