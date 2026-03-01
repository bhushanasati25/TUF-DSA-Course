# Quick Sort Algorithm
# Time Complexity: O(n log n) average, O(n^2) worst | Space Complexity: O(log n)
# In-place, not stable, fastest in practice for most cases

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print(f"Original: {arr}")
    quick_sort(arr, 0, len(arr) - 1)
    print(f"Sorted:   {arr}")
