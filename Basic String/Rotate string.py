"""
📝 Question:
Given two strings s and goal, determine if s can become goal after
performing some number of left shift operations.

Example:
  Input:  s = 'abcde', goal = 'cdeab'
  Output: True
"""

# Check if One String is a Rotation of Another

def rotate_string(s, goal):
    return len(s) == len(goal) and goal in (s + s)


if __name__ == "__main__":
    print(rotate_string("abcde", "cdeab"))  # True
    print(rotate_string("abcde", "abced"))  # False
