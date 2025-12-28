class Solution(object):
    def maximumScore(self, nums, k):
        MOD = 10**9 + 7
        n = len(nums)
        max_num = max(nums)
        prime_factors = [0] * (max_num + 1)
        for i in range(2, max_num + 1):
            if prime_factors[i] == 0:
                for j in range(i, max_num + 1, i):
                    prime_factors[j] += 1

        scores = [prime_factors[num] for num in nums]

        left = [1] * n
        right = [1] * n

        stack = []
        for i in range(n):
            while stack and scores[stack[-1]] < scores[i]:
                stack.pop()
            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and scores[stack[-1]] <= scores[i]:
                stack.pop()
            right[i] = stack[-1] - i if stack else n - i
            stack.append(i)

        idx = list(range(n))
        idx.sort(key=lambda i: -nums[i])

        result = 1
        for i in idx:
            cnt = left[i] * right[i]
            take = min(k, cnt)
            if take == 0:
                break
            result = (result * pow(nums[i], take, MOD)) % MOD
            k -= take

        return result
