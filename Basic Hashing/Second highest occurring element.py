# Second Highest Occurring Element in Array

from collections import Counter

def second_most_frequent(nums):
    count = Counter(nums)
    freqs = sorted(set(count.values()), reverse=True)
    if len(freqs) < 2:
        return -1
    second_freq = freqs[1]
    return min(k for k, v in count.items() if v == second_freq)


if __name__ == "__main__":
    print(second_most_frequent([1, 1, 2, 2, 2, 3]))  # 1
