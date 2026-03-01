# Count of Odd Numbers in Array

def count_odd(arr):
    return sum(1 for x in arr if x % 2 == 1)


if __name__ == "__main__":
    print(count_odd([1, 2, 3, 4, 5]))  # 3
