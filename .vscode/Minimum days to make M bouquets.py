class Solution:
    def possible(self, nums, day, m, k):
        n = len(nums)
        cnt = 0
        noOfB = 0

        for i in range(n):
            if nums[i] <= day:
                cnt += 1
            else:
                noOfB += (cnt // k)

                cnt = 0 

        noOfB += (cnt // k)

        return noOfB >= m 

    def roseGarden(self, n, nums, k, m):
        val = m * k 

        if val > n:
            return -1

        low = min(nums)
        high = max(nums)
        ans = -1 

        while low <= high:
            mid = (low + high) // 2

            if self.possible(nums, mid, m, k):
                ans = mid 
                high = mid - 1
            else:
                low = mid + 1

        return ans

    
     
