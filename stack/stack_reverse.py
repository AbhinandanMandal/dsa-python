
"""Reverse a stack"""


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

    def reverse(self):
        data_list = []
        curr = self.head
        while curr:
            data_list.append(curr.data)
            curr = curr.next

        curr = self.head
        while curr:
            curr.data = data_list.pop()
            curr = curr.next
        return self.head

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
    print("\n")
    stack.display()
    stack.reverse()
    print("\n")
    stack.display()


"""
TODO: Solve this question using recursion 
"""