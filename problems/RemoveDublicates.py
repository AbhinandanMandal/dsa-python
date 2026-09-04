
def RemoveDublicates(array):
    for i in array:
        if array.count(i) > 1:
            array.remove(i)
    return array


array = [1, 2, 2, 3, 4, 4, 5]
print(RemoveDublicates(array))
# Time complexity: O(n)
# Space complexity: O(1)
