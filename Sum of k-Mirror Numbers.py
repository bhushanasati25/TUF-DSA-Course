class Solution(object):
    def kMirror(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        def is_palindrome(s):
            return s == s[::-1]
        
        def to_base_k(num, base):
            result = []
            while num > 0:
                result.append(str(num % base))
                num //= base
            return ''.join(result[::-1])

        def generate_palindromes(length):
            # Half length
            half = (length + 1) // 2
            for i in range(10**(half - 1), 10**half):
                s = str(i)
                # Even length
                if length % 2 == 0:
                    yield int(s + s[::-1])
                else:
                    yield int(s + s[-2::-1])

        count = 0
        total = 0
        length = 1

        while count < n:
            for num in generate_palindromes(length):
                if is_palindrome(to_base_k(num, k)):
                    total += num
                    count += 1
                    if count == n:
                        return total
            length += 1
