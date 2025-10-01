class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        drunk = numBottles
        empties = numBottles
        
        while empties >= numExchange:
            new_bottles = empties // numExchange
            drunk += new_bottles
            empties = empties % numExchange + new_bottles
        
        return drunk
