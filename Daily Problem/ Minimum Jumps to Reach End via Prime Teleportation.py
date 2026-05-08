class Solution(object):
    def minJumps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0
        
        max_val = max(nums)
        if max_val < 2:
            max_val = 2
            
        spf = [i for i in range(max_val + 1)]
        is_prime = [True] * (max_val + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(max_val**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_val + 1, i):
                    is_prime[j] = False
                    if spf[j] == j:
                        spf[j] = i
                        
        prime_to_indices = defaultdict(list)
        for i, val in enumerate(nums):
            temp = val
            while temp > 1:
                p = spf[temp]
                prime_to_indices[p].append(i)
                while temp % p == 0:
                    temp //= p
                    
        queue = deque([0])
        visited = [False] * n
        visited[0] = True
        used_primes = set()
        
        jumps = 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                curr = queue.popleft()
                
                if curr == n - 1:
                    return jumps
                    
                if curr + 1 < n and not visited[curr + 1]:
                    visited[curr + 1] = True
                    queue.append(curr + 1)
                
                if curr - 1 >= 0 and not visited[curr - 1]:
                    visited[curr - 1] = True
                    queue.append(curr - 1)
                    
                val = nums[curr]
                if is_prime[val] and val not in used_primes:
                    used_primes.add(val)
                    for nxt in prime_to_indices[val]:
                        if not visited[nxt]:
                            visited[nxt] = True
                            queue.append(nxt)
            
            jumps += 1
            
        return -1