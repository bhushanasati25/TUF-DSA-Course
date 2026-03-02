"""
📝 Question:
Given the head of a linked list, determine if the linked list has a cycle.
A cycle exists if some node can be reached again by continuously following
the next pointer. Also find the starting node of the cycle if one exists.

Use Floyd's Tortoise and Hare algorithm (O(1) space).
"""

# Detect Cycle in a Linked List (Floyd's Tortoise and Hare)
# Time: O(n) | Space: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def detect_cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None


if __name__ == "__main__":
    # Create: 1 -> 2 -> 3 -> 4 -> back to 2
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = head.next  # Cycle

    print(f"Has Cycle: {'Yes' if has_cycle(head) else 'No'}")

    start = detect_cycle_start(head)
    if start:
        print(f"Cycle starts at node with value: {start.data}")
