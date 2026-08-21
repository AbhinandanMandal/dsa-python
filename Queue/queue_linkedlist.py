"""
# Implementation of queue using array
class Queue:
    def __init__(self, c):
        self.queue = []
        self.capacity = c
        self.front = self.rear = 0

    def enqueue(self, n):
        if self.capacity == self.rear:
            print("Queue full")
        else:
            self.queue.append(n)
            self.rear += 1

    def dequeue(self):
        if self.front == self.rear:
            print("Queue empty")
        else:
            self.queue.pop([0])
            self.rear -= 1

    def display(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            for n in self.queue:
                print(n, '<--', end="")

    def frontelement(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            return self.queue[self.front]


if __name__ == "__main__":
    q = Queue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.display()
"""

# Queue implementation using linked list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isempty(self):
        return self.front is None

    def enqueue(self, n):
        temp_node = Node(n)

        # If queue is empty
        if self.front is None:
            self.front = self.rear = temp_node
            return

        self.rear.next = temp_node
        self.rear = temp_node

    def dequeue(self):

        # At first, we'll check if queue is empty or not
        if self.isempty():
            return

        temp = self.front
        self.front = temp.next

        # If queue becomes empty
        if self.front is None:
            self.rear = None

    def display(self):
        curr = self.front
        while curr:
            print(curr.data, "<--", end="")
            curr = curr.next


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.display()
    q.dequeue()
    q.display()
