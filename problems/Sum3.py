
def Sum3(array: list):
    array.sort()
    result = []

    for i in range(len(array)-2):
        if i > 0 and array[i] == array[i-1]:
            continue
        left = i+1
        right = len(array)-1

        while left < right:
            total = array[i]+array[left]+array[right]
            if total == 0:
                result.append([array[i], array[left], array[right]])
                left += 1
                right -= 1

                # Skipping dublicates from left
                while left < right and array[left] == array[left-1]:
                    left += 1
                # Skipping dublicates from right
                while left < right and array[right] == array[right+1]:
                    right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1
    return result


print(Sum3([-1, 0, 1, 2, -1, -4]))

""" 
Sorting: O(nlogn) Tim sort
Main search: O(n^2)
Total: O(n^2)

"""