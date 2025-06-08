class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []

        def dfs(curr):
            if curr > n:
                return

            result.append(curr)

            # Try appending digits 0-9
            for i in range(10):
                next_num = curr * 10 + i
                if next_num <= n:
                    dfs(next_num)
                else:
                    if i == 0:
                        continue # If current number is already too big, don't try appending 0
                    else:
                        break # If current number + 0 is too big, then current number + 1,2.. will also be too big

        # Start DFS for numbers 1-9
        for i in range(1, 10):
            dfs(i)

        return result