# Reverse a Number

def reverse_number(n):
    rev = 0
    neg = n < 0
    n = abs(n)
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return -rev if neg else rev


if __name__ == "__main__":
    print(reverse_number(12345))  # 54321
    print(reverse_number(100))    # 1
