# Check if a String is Palindrome

def is_palindrome(s):
    return s == s[::-1]


if __name__ == "__main__":
    print(is_palindrome("racecar"))  # True
    print(is_palindrome("hello"))    # False
