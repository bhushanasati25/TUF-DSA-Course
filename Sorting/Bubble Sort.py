# Bubble Sort Algorithm
# Time: O(n^2) | Space: O(1) | Optimized with early break

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Sorted: {bubble_sort(arr)}")
