
"""
We can use efficient quick sort algorithm for this. 
Below the implementation of quick sort algorithm using hoare's algorithm
"""

"""
def hoare_partition(arr, low, high):
    i = low-1
    j = high+1
    pivot = arr[low]
    while True:
        i += 1
        while (arr[i] < pivot):
            i += 1
        j -= 1
        while (arr[j] > pivot):
            j -= 1

        if (i >= j):
            return j

        arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr, low, high):
    if (high > low):
        p = hoare_partition(arr, low, high)
        quick_sort(arr, low, p)
        quick_sort(arr, p+1, high)
    return arr


nums = quick_sort([5, 13, 6, 9, 12, 8, 11], 0, 6)
print(nums)

# Time complexity: O(nlogn), Space complexity: O(logn)

"""

from collections import deque
stack = deque()

stack.append(3)
stack.append(1)
stack.append(4)
stack.append(2)


def hoare_partition(arr, low, high):
    i = low-1
    j = high+1
    pivot = arr[low]
    while True:
        i += 1
        while (arr[i] < pivot):
            i += 1
        j -= 1
        while (arr[j] > pivot):
            j -= 1
        if (i >= j):
            return j
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr, low, high):
    if (high > low):
        p = hoare_partition(arr=arr, low=low, high=high)
        quick_sort(arr=arr, low=low, high=p)
        quick_sort(arr=arr, low=p+1, high=high)
    return arr


def sort_stack(stack):
    stack_nums = [n for n in stack]
    sorted_nums = quick_sort(stack_nums, 0, len(stack_nums)-1)
    return sorted_nums


print(sort_stack(stack=stack))
