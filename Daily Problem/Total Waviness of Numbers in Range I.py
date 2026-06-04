class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def get_waviness(x):
            nums = []
            while x > 0:
                nums.append(x % 10)
                x //= 10
            
            m = len(nums)
            if m < 3:
                return 0
            
            waviness = 0
            for i in range(1, m - 1):
                if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                    waviness += 1
                elif nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                    waviness += 1
                    
            return waviness

        return sum(get_waviness(x) for x in range(num1, num2 + 1))