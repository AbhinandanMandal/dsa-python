
""" 
The Longest Even-Odd Subarray problem is a common array problem where you need 
to find the length of the longest contiguous subarray in which even and odd numbers alternate.

Example
array = [5, 10, 20, 6, 3, 8, 7, 4]

Let's look at the subarrays:
[5, 10]             → odd, even 
[10, 20]            → even, even 
[3, 8, 7, 4]        → odd, even, odd, even (longest)
So the answer is: 4
because [3, 8, 7, 4] has the longest alternating pattern.
"""


"""# Not a good solution
def LongestOddEven(array):
    max_count = 0
    count_even_odd = 0
    count_odd_even = 0
    for i in range(len(array)-1):
        if array[i] % 2 == 0 and array[i+1] % 2 != 0:
            count_even_odd += 2
            max_count = max(max_count, count_even_odd)
        elif array[i] % 2 != 0 and array[i+1] % 2 == 0:
            count_odd_even += 2
            max_count = max(max_count, count_odd_even)
        else:
            count_even_odd = 0
            count_odd_even = 0
    return max_count


array = [5, 10, 20, 6, 3, 8, 7, 4]
print(LongestOddEven(array))"""

# Optimal solution


def LongestEvenOdd(array):
    count = 1
    max_count = 1
    for i in range(1, len(array)):
        if array[i] % 2 != array[i-1] % 2:
            count += 1
        else:
            count = 1
    return max(max_count, count)


# array = [5, 10, 20, 6, 3, 8, 7, 4]
array = [1, 2, 3, 4, 5]
print(LongestEvenOdd(array))
# Time complexity: O(n)
# Space complexity: O(1)
