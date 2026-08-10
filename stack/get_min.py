
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        # updating this value everytime during push() operation
        self.minEle = float("inf")

    def push(self, n):
        new_node = Node(n)
        if new_node.data < self.minEle:
            self.minEle = new_node.data

        new_node.next = self.head
        self.head = new_node

    def pop(self):
        pop_node = self.head
        self.head = pop_node.next
        pop_node.next = None
        return pop_node.data

    def peek(self):
        return self.head.data

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next

    def isEmpty(self):
        return self.head is None

    # O(1) approach
    def getMin(self):
        return self.minEle

    """ 
    # O(n) approach
    def getMin(self):
        curr = self.head
        elements = []
        while curr:
            elements.append(curr.data)
            curr = curr.next

        return min(elements)
    """


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    print("\nMinimum Element")
    print(stack.getMin())
