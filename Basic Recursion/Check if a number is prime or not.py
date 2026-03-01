# Check if a Number is Prime (Recursive)

import math

def is_prime(n, x=2):
    if n <= 1:
        return False
    if x > math.isqrt(n):
        return True
    if n % x == 0:
        return False
    return is_prime(n, x + 1)


if __name__ == "__main__":
    for num in [2, 7, 10, 13]:
        print(f"{num}: {'Prime' if is_prime(num) else 'Not Prime'}")
