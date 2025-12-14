class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        MOD = 10**9 + 7
        seats = []
        for i in range(len(corridor)):
            if corridor[i] == 'S':
                seats.append(i)

        total_seats = len(seats)

        if total_seats < 2 or total_seats % 2 == 1:
            return 0

        if total_seats == 2:
            return 1

        ways = 1
        for i in range(1, total_seats // 2):
            left = seats[2 * i - 1]
            right = seats[2 * i]
            gap = right - left - 1  
            ways = (ways * (gap + 1)) % MOD

        return ways
