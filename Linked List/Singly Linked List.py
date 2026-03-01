# Singly Linked List - Basic Operations
# Insert at head, tail | Delete | Display | Reverse | Length

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, val):
        new_node = Node(val)
        new_node.next = self.head
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

    def delete_node(self, val):
        if not self.head:
            return
        if self.head.data == val:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next and temp.next.data != val:
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next

    def reverse(self):
        prev, curr = None, self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def length(self):
        count, temp = 0, self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def display(self):
        elements = []
        temp = self.head
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(elements) + " -> NULL")


if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.insert_at_tail(10)
    ll.insert_at_tail(20)
    ll.insert_at_tail(30)
    ll.insert_at_head(5)

    print("Linked List: ", end="")
    ll.display()
    print(f"Length: {ll.length()}")

    ll.delete_node(20)
    print("After deleting 20: ", end="")
    ll.display()

    ll.reverse()
    print("Reversed: ", end="")
    ll.display()
