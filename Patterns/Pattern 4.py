# Pattern 4: Right Triangle with Row Number
# 1
# 2 2
# 3 3 3
# 4 4 4 4

def pattern4(n):
    for i in range(1, n + 1):
        print((str(i) + " ") * i)

pattern4(5)
