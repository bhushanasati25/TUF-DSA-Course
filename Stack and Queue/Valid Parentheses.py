# Valid Parentheses - Check if brackets are balanced
# Uses stack to match opening and closing brackets
# Time: O(n) | Space: O(n)

def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()

    return len(stack) == 0


if __name__ == "__main__":
    tests = ["({[]})", "({[})", "((()))"]
    for t in tests:
        print(f"{t} -> {'Valid' if is_valid(t) else 'Invalid'}")
