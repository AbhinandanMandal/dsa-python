
"""
def balancedParenthesis(expression):
    open_list = ["{", "[", "("]
    close_list = ["}", "]", ")"]
    stack = []

    for char in expression:
        if char in open_list:
            stack.append(char)

        elif char in close_list:
            pos = close_list.index(char)

            if stack and stack[-1] == open_list[pos]:
                stack.pop()
            else:
                return "Unbalanced"
    return "Balanced" if not stack else "Unbalanced"


print(balancedParenthesis("{[]{()}}"))

# Time complexity: O(N)
# Space complexity: O(1)

"""


def BalancedParenthesis(expression):
    opening = ["{", "[", "("]
    closing = ["}", "]", ")"]
    stack = []

    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            pos = closing.index(char)

            if stack and stack[-1] == opening[pos]:
                stack.pop()
            else:
                return "Unbalanced"
    return "Balanced" if not stack else "Unbalanced"


print(BalancedParenthesis("{[]{()}}"))
