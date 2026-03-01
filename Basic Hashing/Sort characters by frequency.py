# Sort Characters by Frequency

from collections import Counter

def frequency_sort(s):
    count = Counter(s)
    # Sort by frequency (desc), then alphabetically
    return sorted(count.keys(), key=lambda c: (-count[c], c))


if __name__ == "__main__":
    print(frequency_sort("tree"))    # ['e', 'r', 't']
    print(frequency_sort("aabbcc")) # ['a', 'b', 'c']
