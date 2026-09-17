
""" 
Bubble sort: 
simplest sorting algorithm, it's `stable` and `in-place`.

Basic of Bubble sort is: it chooses the large value and put it in the end position of the array and keep doing it 
                         untill it become sorted array.
"""


def BubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


array = [10, 8, 20, 5]
print(BubbleSort(array))

# Time complexity: O(n^2)
# Space complexity: O(1)