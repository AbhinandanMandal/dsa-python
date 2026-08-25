
from collections import deque
stack = deque()


def is_paliendrome(array):
    stack = deque(array)
    paliendrome = True
    while len(stack) > 1:
        if stack.pop() != stack.popleft():
            paliendrome = False
            break
    return paliendrome


print(is_paliendrome([1, 2, 3, 2, 1]))
