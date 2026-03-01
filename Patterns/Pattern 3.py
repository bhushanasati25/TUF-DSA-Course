# Pattern 3: Right Triangle of Numbers
# 1
# 1 2
# 1 2 3
# 1 2 3 4

def pattern3(n):
    for i in range(1, n + 1):
        print(" ".join(str(j) for j in range(1, i + 1)))

pattern3(5)
