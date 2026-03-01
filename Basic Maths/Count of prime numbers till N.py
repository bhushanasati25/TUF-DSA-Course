# Count of Prime Numbers up to N

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def count_primes(n):
    return sum(1 for i in range(2, n + 1) if is_prime(i))


if __name__ == "__main__":
    print(count_primes(20))  # 8 (2,3,5,7,11,13,17,19)
