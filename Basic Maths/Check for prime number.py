# Check if a Number is Prime

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


if __name__ == "__main__":
    for num in [2, 7, 10, 13, 1]:
        print(f"{num}: {'Prime' if is_prime(num) else 'Not Prime'}")
