"""
📝 Question:
Implement a Stack data structure with the following operations:
  1. push(val) — Add element to top
  2. pop() — Remove and return top element
  3. top() — Return top element without removing
  4. is_empty() — Check if stack is empty
  5. size() — Return number of elements

Follow LIFO (Last In, First Out) principle.
"""

# Stack Implementation using List
# LIFO (Last In First Out)
# Operations: push, pop, top, is_empty, size

class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if self.is_empty():
            print("Stack Underflow!")
            return None
        return self.items.pop()

    def top(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)

    print(f"Top: {s.top()}")
    print(f"Size: {s.size()}")
    print(f"Popped: {s.pop()}")
    print(f"Top after pop: {s.top()}")
