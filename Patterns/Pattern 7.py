"""
📝 Question:
Print a centered pyramid of stars.

For n = 4:
     *
    ***
   *****
  *******
"""

# Pattern 7: Pyramid of Stars
#     *
#    ***
#   *****
#  *******
# *********

def pattern7(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "* " * (2 * i - 1)
        print(spaces + stars.strip() + spaces)

pattern7(5)
