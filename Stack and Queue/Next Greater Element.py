# Next Greater Element using Stack
# For each element, find the next greater element to its right
# Time: O(n) | Space: O(n)

def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = []  # Monotonic decreasing stack

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])

    return result


if __name__ == "__main__":
    arr = [4, 5, 2, 10, 8]
    result = next_greater_element(arr)

    print(f"Array:               {arr}")
    print(f"Next Greater Element: {result}")
