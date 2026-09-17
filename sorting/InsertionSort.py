
"""
insertion sort is `stable` and `in-place` sorting algorithm

It works on a hypothesis that, it let, some portion of list is sorted and some unsorted
then it sort the whole list untill it become fully sorted. Imagine it like when we sort deck of cards one by one
"""

def InsertionSort(array):
    for i in range(1, len(array)):
        key=array[i]
        j=i-1
        while (j>=0 and array[j]>key):
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key 
    return array


array=[5,2,4,6,1,3]
print(InsertionSort(array))
