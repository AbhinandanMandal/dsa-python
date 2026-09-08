
def WaterContainer(array):
    max_water = 0
    left = 0
    right = len(array)-1

    while left < right:
        width = right-left
        height = min(array[right], array[left])
        water = width*height
        max_water = max(max_water, water)

        if array[left] < array[right]:
            left += 1
        else:
            right -= 1
    return max_water


array = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(WaterContainer(array))

# Time complexity: O(n), Space complexity: O(1)
