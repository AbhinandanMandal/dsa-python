

def MajorityElement(array: list):
    array_hash = {}
    n = len(array)
    for i in array:
        array_hash[i] = array_hash.get(i, 0)+1

    for k, v in array_hash.items():
        if v > (n/2):
            return k


arr = [2, 2, 1, 1, 1, 2, 2]
print(MajorityElement(arr))

# Time and space complexity O(n)
