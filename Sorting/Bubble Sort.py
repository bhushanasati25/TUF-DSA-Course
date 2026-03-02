"""
📝 Question:
Implement the Bubble Sort algorithm.
Repeatedly swap adjacent elements if they are in the wrong order.
Optimize with an early break if no swaps occur in a pass.

Time: O(n²) | Space: O(1) | Stable

Example:
  Input:  [64, 34, 25, 12, 22, 11, 90]
  Output: [11, 12, 22, 25, 34, 64, 90]
"""

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
