
# Queue implementation using Array
# Queue follows FIFO (First In First Out) principle

class Queue:
    def __init__(self, c):
        self.queue = []
        self.capacity = c
        self.front = self.rear = 0

    def Enqueue(self, data):  # Insertion
        if self.capacity == self.rear:
            print("Queue is full")
        else:
            self.queue.append(data)
            self.rear += 1  # Increasing rear by 1 position

    def Dequeue(self):  # Deletion
        if self.front == self.rear:
            print("Queue is empty")
        else:
            self.queue.pop(0)  # Queue follows FIFO principle
            self.rear -= 1

    def display(self):
        if self.front == self.rear:
            print("Queue is empty")
            return
        else:
            for n in self.queue:
                print(n, "<--", end="")

    def queueFront(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            print(self.queue[self.front])


if __name__ == "__main__":
    q = Queue(5)
    q.Enqueue(1)
    q.Enqueue(2)
    q.Enqueue(3)
    q.Enqueue(4)
    q.display()
    q.Dequeue()
    q.display()
    q.queueFront()
