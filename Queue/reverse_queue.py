
# If we implement queue using linked list then reversing a queue is generally reversing a linked list

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

        if self.isempty():
            self.front = self.rear = temp_node

        # else
        self.rear.next = temp_node
        self.rear = temp_node

    def dequeue(self):
        if self.isempty():
            return

        # else
        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None

        return temp.data

    def reverse(self):
        curr = self.front
        elements = []
        while curr:
            elements.append(curr.data)
            curr = curr.next

        curr = self.front
        while curr:
            curr.data = elements.pop()
            curr = curr.next

        return self.front

    def display(self):
        curr = self.front
        while curr:
            print(curr.data, end=" ")
            curr = curr.next


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.display()
    print("\n")
    q.reverse()
    q.display()
