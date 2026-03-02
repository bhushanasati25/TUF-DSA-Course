"""
📝 Question:
Given a positive integer n, check if it is an Armstrong number.
An Armstrong number of d digits satisfies: sum of each digit raised
to the power d equals the number itself.

Example:
  Input:  153
  Output: True  (1³ + 5³ + 3³ = 1 + 125 + 27 = 153)
"""

# Check if a Number is Armstrong
# Armstrong: sum of digits^(number of digits) == number

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return sum(int(d) ** power for d in digits) == n


if __name__ == "__main__":
    print(is_armstrong(153))   # True (1^3+5^3+3^3=153)
    print(is_armstrong(370))   # True
    print(is_armstrong(123))   # False
