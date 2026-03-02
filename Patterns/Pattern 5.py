"""
📝 Question:
Print an inverted right-angled triangle of stars.

For n = 4:
  * * * *
  * * *
  * *
  *
"""

# Pattern 5: Inverted Right Triangle of Stars
# * * * * *
# * * * *
# * * *
# * *
# *

def pattern5(n):
    for i in range(n, 0, -1):
        print("* " * i)

pattern5(5)
