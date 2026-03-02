"""
📝 Question:
Given two strings s and goal, return True if s can become goal after some
number of shifts (rotations) on s. A shift moves the leftmost character
to the rightmost position.

Example:
  Input:  s = 'abcde', goal = 'cdeab'
  Output: True
"""

# Check if One String is a Rotation of Another

def rotate_string(s, goal):
    if len(s) != len(goal):
        return False
    return goal in (s + s)


if __name__ == "__main__":
    print(rotate_string("abcde", "cdeab"))  # True
    print(rotate_string("abcde", "abced"))  # False
