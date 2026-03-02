"""
📝 Question:
Implement a Queue data structure with the following operations:
  1. enqueue(val) — Add element to rear
  2. dequeue() — Remove and return front element
  3. front() — Return front element without removing
  4. is_empty() — Check if queue is empty
  5. size() — Return number of elements

Follow FIFO (First In, First Out) principle.
"""

# Queue Implementation using collections.deque
# FIFO (First In First Out)
# Operations: enqueue, dequeue, front, is_empty, size

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.items.popleft()

    def front(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print(f"Front: {q.front()}")
    print(f"Dequeued: {q.dequeue()}")
    print(f"Front after dequeue: {q.front()}")
    print(f"Size: {q.size()}")
