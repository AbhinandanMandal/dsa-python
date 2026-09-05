
"""def MoveZeros(array: list):

    i = 0
    while i < len(array):
        if array[i] == 0:
            num = array.pop(i)
            array.append(num)
            i += 1
        else:
            i += 1
    return array


array = [1, 0, 2, 0, 3]
print(MoveZeros(array))

But the above solution is problematic and can 
produce upto O(n^2) time complexity

"""

# A more compact and effective solution in this would be


def MoveZeros(array: list):
    insert_pos = 0

    for i in range(len(array)):
        if array[i] != 0:
            array[insert_pos] = array[i]
            insert_pos += 1

    while insert_pos < len(array):
        array[insert_pos] = 0
        insert_pos += 1

    return array


array = [1, 0, 2, 0, 3]
print(MoveZeros(array))
