"""
📝 Question:
Given a string s containing only '(', ')', '{', '}', '[' and ']',
determine if the input string has valid (balanced) brackets.

Rules:
  - Every open bracket must be closed by the same type of bracket
  - Open brackets must be closed in the correct order

Example:
  Input:  '({[]})'
  Output: True

  Input:  '({[})'
  Output: False
"""

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
