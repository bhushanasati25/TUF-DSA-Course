"""
📝 Question:
Implement a Doubly Linked List with the following operations:
  1. Insert at head
  2. Insert at tail
  3. Delete a node by value
  4. Display forward (head → tail)
  5. Display backward (tail → head)
"""

# Doubly Linked List - Basic Operations
# Insert at head, tail | Delete | Display forward & backward

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, val):
        new_node = Node(val)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_tail(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def delete_node(self, val):
        temp = self.head
        while temp and temp.data != val:
            temp = temp.next
        if not temp:
            return
        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next
        if temp.next:
            temp.next.prev = temp.prev

    def display_forward(self):
        elements = []
        temp = self.head
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        print("Forward:  " + " <-> ".join(elements) + " <-> NULL")

    def display_backward(self):
        if not self.head:
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        elements = []
        while temp:
            elements.append(str(temp.data))
            temp = temp.prev
        print("Backward: " + " <-> ".join(elements) + " <-> NULL")


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_tail(10)
    dll.insert_at_tail(20)
    dll.insert_at_tail(30)
    dll.insert_at_head(5)

    dll.display_forward()
    dll.display_backward()

    dll.delete_node(20)
    print("After deleting 20:")
    dll.display_forward()
