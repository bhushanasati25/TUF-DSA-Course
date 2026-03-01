# Pattern 8: Inverted Pyramid of Stars
# *********
#  *******
#   *****
#    ***
#     *

def pattern8(n):
    for i in range(n, 0, -1):
        spaces = " " * (n - i)
        stars = "* " * (2 * i - 1)
        print(spaces + stars.strip() + spaces)

pattern8(5)
