"""
📝 Question:
Print a butterfly pattern.

For n = 4:
  *      *
  **    **
  ***  ***
  ********
  ***  ***
  **    **
  *      *
"""

# Pattern 20: Butterfly Pattern
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

def pattern20(n):
    for i in range(1, 2 * n):
        stars = i if i <= n else 2 * n - i
        spaces = 2 * (n - stars)
        print("*" * stars + " " * spaces + "*" * stars)

pattern20(5)
