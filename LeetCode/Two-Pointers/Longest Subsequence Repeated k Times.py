from collections import deque

class Solution(object):
    def longestSubsequenceRepeatedK(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        def is_k_subsequence(word):
            count = 0
            j = 0
            for ch in s:
                if ch == word[j]:
                    j += 1
                    if j == len(word):
                        count += 1
                        j = 0
                if count == k:
                    return True
            return False

        # Count frequency of characters in s
        from collections import Counter
        freq = Counter(s)
        # Only keep characters that appear at least k times
        valid_chars = [ch for ch in freq if freq[ch] >= k]
        valid_chars.sort(reverse=True)  # for lexicographical order

        q = deque([""])
        ans = ""

        while q:
            curr = q.popleft()
            for ch in valid_chars:
                new_seq = curr + ch
                if is_k_subsequence(new_seq):
                    q.append(new_seq)
                    # Update answer if longer or lexicographically larger at same length
                    if len(new_seq) > len(ans) or (len(new_seq) == len(ans) and new_seq > ans):
                        ans = new_seq

        return ans
