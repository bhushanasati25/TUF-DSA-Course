# Pattern 10: Arrow (Triangle + Inverted Triangle)

def pattern10(n):
    # Upper half
    for i in range(1, n + 1):
        print("*" * i)
    # Lower half
    for i in range(n - 1, 0, -1):
        print("*" * i)

pattern10(5)
