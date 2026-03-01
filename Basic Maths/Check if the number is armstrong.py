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
