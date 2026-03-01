# Reverse an Array

def reverse_array(arr):
    return arr[::-1]


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(f"Original: {arr}")
    print(f"Reversed: {reverse_array(arr)}")
