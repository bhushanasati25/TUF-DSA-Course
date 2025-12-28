import math

class Solution(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """
        # Binary search range: minimum time (1) to max possible time (worst worker does all repairs)
        left, right = 1, min(ranks) * cars * cars  

        def canRepairInTime(T):
            total_cars = 0
            for r in ranks:
                total_cars += int(math.sqrt(T // r))  # Cars a worker can repair in T time
                if total_cars >= cars:
                    return True  # If we can repair all cars within T, return True
            return False

        while left < right:
            mid = (left + right) // 2
            if canRepairInTime(mid):
                right = mid  # Try a smaller time
            else:
                left = mid + 1  # Increase time

        return left  # Minimum time to repair all cars
