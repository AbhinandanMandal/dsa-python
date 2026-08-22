
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

        # If queue is empty then
        if self.front is None:
            self.front = self.rear = temp_node
            return
        # else
        self.rear.next = temp_node
        self.rear = temp_node

    def dequeue(self):
        if self.isempty():
            return

        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None

        return temp.data


def generate_binary(num):
    q = Queue()
    q.enqueue("1")

    for _ in range(num):
        current = q.dequeue()
        print(current, end=" ")

        q.enqueue(current+"0")
        q.enqueue(current+"1")


generate_binary(5)
