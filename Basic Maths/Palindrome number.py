# Check if a Number is Palindrome

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


if __name__ == "__main__":
    print(is_palindrome(121))   # True
    print(is_palindrome(123))   # False
