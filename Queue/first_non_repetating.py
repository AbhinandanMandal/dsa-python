
# For CP, it is always advisable to use dequeue() for faster work done
from collections import deque


def FirstNonRepetating(stream):
    queue = deque()
    freq = {}

    for char in stream:
        # Check the frquency of the character for non-repetation
        freq[char] = freq.get(char, 0)+1
        queue.append(char)

        while queue and freq[queue[0]] > 1:
            queue.popleft()

        if queue:
            print(queue[0], end=" ")
        else:
            print("#", end=" ")


FirstNonRepetating("aabc")
