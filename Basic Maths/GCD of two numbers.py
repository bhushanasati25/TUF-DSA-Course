# GCD (Greatest Common Divisor) of Two Numbers

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    print(gcd(12, 8))   # 4
    print(gcd(54, 24))  # 6
