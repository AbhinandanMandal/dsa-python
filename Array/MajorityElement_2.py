
# Majority element problem can be solved by Boyer-Moore voting algorithm
def MajorityElement(array):
    candidate = None
    count = 0
    for num in array:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate


arr = [2, 2, 1, 1, 1, 2, 2]
print(MajorityElement(arr))
