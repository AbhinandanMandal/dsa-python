
# Finding subarray of an array
def Subarray(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            print(array[i:j+1])


Subarray([1, 2, 3])
