
# We can solve this question using stack

def BalancedParenthesis(parenthesis: str):
    open_braces = ["{", "[", "("]
    close_braces = ["}", "]", ")"]
    stack = []

    for char in parenthesis:
        if char in open_braces:
            stack.append(char)
        elif char in close_braces:
            pos = close_braces.index(char)

            if stack and stack[-1] == open_braces[pos]:
                stack.pop()
            else:
                return "Unbalanced"
    return "Balanced" if not stack else "Unbalanced"


print(BalancedParenthesis("{[]{()}}"))
