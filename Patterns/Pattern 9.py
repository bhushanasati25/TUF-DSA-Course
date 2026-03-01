# Pattern 9: Diamond of Stars (Pyramid + Inverted)

def pattern9(n):
    # Upper pyramid
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    # Lower inverted pyramid
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

pattern9(5)
