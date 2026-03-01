# Sum of Array Elements (Recursive)

def array_sum(arr, index=0):
    if index >= len(arr):
        return 0
    return arr[index] + array_sum(arr, index + 1)


if __name__ == "__main__":
    print(array_sum([1, 2, 3, 4, 5]))  # 15
