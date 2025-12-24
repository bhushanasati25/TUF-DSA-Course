class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        total_apples = sum(apple)

       
        capacity.sort(reverse=True)

        boxes_used = 0
        for cap in capacity:
            total_apples -= cap
            boxes_used += 1
            if total_apples <= 0:
                return boxes_used
