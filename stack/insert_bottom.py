
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, n):
        new_node = Node(n)
        new_node.next = self.head
        self.head = new_node
        return new_node

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next

    def insert_bottom(self, n):
        new_node = Node(n)
        curr = self.head
        while curr.next:
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        return self.head


if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(10)
    stack.push(15)
    stack.display()
    stack.insert_bottom(2)
    print('\n')
    stack.display()
