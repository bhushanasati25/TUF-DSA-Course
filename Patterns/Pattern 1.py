"""
📝 Question:
Print a square pattern of stars (n × n).

For n = 4:
  * * * *
  * * * *
  * * * *
  * * * *
"""

# Pattern 1: Square of Stars
# * * * *
# * * * *
# * * * *
# * * * *

def pattern1(n):
    for i in range(n):
        print("* " * n)

pattern1(5)
