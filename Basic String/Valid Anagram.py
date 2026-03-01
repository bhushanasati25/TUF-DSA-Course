# Valid Anagram Check

def is_anagram(s, t):
    return sorted(s) == sorted(t)


if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))  # True
    print(is_anagram("rat", "car"))          # False
