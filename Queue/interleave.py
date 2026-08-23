
from collections import deque


def Interleave(array: list):
    queue1 = deque(array[0:len(array)//2])
    queue2 = deque(array[len(array)//2:])
    interleaved = []
    while (queue1 and queue2):
        interleaved.append(queue1.popleft())
        interleaved.append(queue2.popleft())
    return interleaved


print(Interleave([1, 2, 3, 4, 5, 6]))
