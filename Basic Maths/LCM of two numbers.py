# LCM (Least Common Multiple) of Two Numbers

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)


if __name__ == "__main__":
    print(lcm(12, 8))   # 24
    print(lcm(5, 7))    # 35
