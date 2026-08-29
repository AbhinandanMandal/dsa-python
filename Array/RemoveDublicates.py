
# Remove dublicates from a sorted array

def removedublicates(array: list):
    for n in array:
        if array.count(n) > 1:
            array.remove(n)
    return array


array = [1, 2, 2, 3, 4, 4, 5]
print(removedublicates(array))

# Time complexity: O(n)
# Space complexity: O(1)

