"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        popped = self.head
        self.head = self.head.next
        popped.next = None
        return popped.data

    def peek(self):
        peek_element = self.head
        return peek_element.data

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next


# Driver code
if __name__ == "__main__":
    stack = Stack()
    print("Pushing into stack")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    print("Popping through stack")
    stack.pop()
    stack.display()
    print(stack.peek())

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        popped = self.head
        self.head = self.head.next
        popped.next = None
        return popped.data

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next

    def peek(self):
        return self.head.data


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Displaying stack")
    stack.display()

    print("Popping stack")
    stack.pop()
    print("Displaying after single pop()")
    stack.display()

    print("Peek stack")
    print(stack.peek())
