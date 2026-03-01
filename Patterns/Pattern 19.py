# Pattern 19: Symmetric Star Pattern (Hourglass sides)
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# **      **
# ***    ***
# ****  ****
# **********

def pattern19(n):
    # Upper half
    for i in range(n):
        stars = "*" * (n - i)
        spaces = " " * (2 * i)
        print(stars + spaces + stars)
    # Lower half
    for i in range(n - 2, -1, -1):
        stars = "*" * (n - i)
        spaces = " " * (2 * i)
        print(stars + spaces + stars)

pattern19(5)
