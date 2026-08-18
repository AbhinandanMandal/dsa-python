
from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, n):
        self.stack.append(n)
        return self.stack

    def delete_midelement(self):
        stack_nums = [n for n in self.stack]
        return stack_nums[len(self.stack)//2]


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack.delete_midelement())
