# Check if a Number is Perfect
# A perfect number equals the sum of its proper divisors

def is_perfect(n):
    if n <= 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n


if __name__ == "__main__":
    print(is_perfect(28))   # True (1+2+4+7+14=28)
    print(is_perfect(12))   # False
