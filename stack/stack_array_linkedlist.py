

"""
stack follows LIFO (Last In First Out) principle
"""

"""
# Stack using list
class Stack:
    def __init__(self):
        self.stack_array = []

    def isEmpty(self):
        return self.stack_array is None

    def push(self, n):
        self.stack_array.append(n)
        return self.stack_array

    def pop(self):
        if not self.isEmpty():
            return self.stack_array.pop()

    def peek(self):
        if not self.isEmpty():
            return self.stack_array[0]


stack = Stack()
print(stack.push(10))
print(stack.push(20))
print(stack.push(30))
print(stack.pop())
print(stack.peek())
"""


# Stack using linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def push(self, n):
        new_node = Node(n)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        popped = self.head
        self.head = popped.next
        popped.next = None
        return popped.data

    def peek(self):
        return self.head.data

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    print("\n")
    print(stack.pop())
    print("\n")
    print(stack.peek())
    stack.display()
