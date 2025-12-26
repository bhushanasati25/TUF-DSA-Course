class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        max_profit = 0
        profit = 0
        best_time = 0

        for i, c in enumerate(customers):
            if c == 'Y':
                profit += 1
            else:
                profit -= 1
                
            if profit > max_profit:
                max_profit = profit
                best_time = i + 1

        return best_time
