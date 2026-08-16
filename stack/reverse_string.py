
""" Reverse a string using stack """


# One of the very simple method using list
def reverse_string(string):
    string_list = list(string)
    string_list = string_list[::-1]
    return "".join(string_list)


print(reverse_string("hello"))



# Using stack
def ReverseString(string):
    string_list = list(string)
    reverse_string = []
    while string_list:
        reverse_string.append(string_list.pop())
    return "".join(reverse_string)


print(ReverseString("Hello"))
# Time complexity: O(n)
# Space complexity: O(n)

