# Sum of Highest and Lowest Frequency in Array

from collections import Counter

def sum_high_low_freq(nums):
    count = Counter(nums)
    freqs = count.values()
    return max(freqs) + min(freqs)


if __name__ == "__main__":
    print(sum_high_low_freq([1, 1, 2, 2, 2, 3]))  # 4 (3+1)
