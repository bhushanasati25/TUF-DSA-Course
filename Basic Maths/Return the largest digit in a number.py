# Return the Largest Digit in a Number

def largest_digit(n):
    return max(int(d) for d in str(abs(n)))


if __name__ == "__main__":
    print(largest_digit(38294))  # 9
