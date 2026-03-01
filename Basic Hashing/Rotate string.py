# Check if One String is a Rotation of Another

def rotate_string(s, goal):
    if len(s) != len(goal):
        return False
    return goal in (s + s)


if __name__ == "__main__":
    print(rotate_string("abcde", "cdeab"))  # True
    print(rotate_string("abcde", "abced"))  # False
