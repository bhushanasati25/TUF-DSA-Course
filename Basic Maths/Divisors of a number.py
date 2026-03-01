# Find All Divisors of a Number

def divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]


if __name__ == "__main__":
    print(divisors(12))  # [1, 2, 3, 4, 6, 12]
