"""
# A classic two loops solution
def WaterContainer(array: list):
    max_water = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            width = j-i
            height = min(array[j], array[i])
            water = width*height
            max_water = max(max_water, water)
    return max_water


array = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(WaterContainer(array))
# Time complexity: O(n^2), Space complexity: O(1)"""


def WaterContainer(array: list):
    max_water = 0
    left = 0
    right = len(array)-1

    while left < right:
        width = right-left
        water_height = min(array[right], array[left])
        water = width*water_height
        max_water = max(max_water, water)

        if array[left] < array[right]:
            left += 1
        else:
            right -= 1
    return max_water


array = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(WaterContainer(array))

# Time complexity: O(n), Space complexity: O(1)
